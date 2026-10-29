import AppKit
import WebKit
// usage: snap <url> <out.png> <width> [dark]
let args = CommandLine.arguments
let url = URL(string: args[1])!, out = args[2], width = CGFloat(Double(args[3])!)
let dark = args.count > 4
let app = NSApplication.shared
class Loader: NSObject, WKNavigationDelegate {
    let web: WKWebView
    init(_ w: WKWebView) { web = w }
    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        DispatchQueue.main.asyncAfter(deadline: .now() + 1.5) {
            webView.evaluateJavaScript("document.documentElement.scrollHeight") { h, _ in
                let height = (h as? CGFloat) ?? 2000
                webView.frame = NSRect(x: 0, y: 0, width: width, height: height)
                DispatchQueue.main.asyncAfter(deadline: .now() + 1.5) {
                    let cfg = WKSnapshotConfiguration()
                    cfg.rect = NSRect(x: 0, y: 0, width: width, height: height)
                    webView.takeSnapshot(with: cfg) { img, err in
                        guard let img, let tiff = img.tiffRepresentation, let rep = NSBitmapImageRep(data: tiff),
                              let png = rep.representation(using: .png, properties: [:]) else { print(err ?? "fail"); exit(1) }
                        try! png.write(to: URL(fileURLWithPath: out)); print("ok \(Int(height))"); exit(0)
                    }
                }
            }
        }
    }
}
let window = NSWindow(contentRect: NSRect(x: 0, y: 0, width: width, height: 900), styleMask: [.borderless], backing: .buffered, defer: false)
if dark { window.appearance = NSAppearance(named: .darkAqua) } else { window.appearance = NSAppearance(named: .aqua) }
let web = WKWebView(frame: NSRect(x: 0, y: 0, width: width, height: 900))
window.contentView = web
let loader = Loader(web); web.navigationDelegate = loader
web.load(URLRequest(url: url))
app.run()
