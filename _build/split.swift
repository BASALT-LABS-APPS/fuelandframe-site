import AppKit
// split <in.png> <outPrefix> <targetWidth> <pieceHeight>
let a = CommandLine.arguments
let img = NSImage(contentsOfFile: a[1])!
let rep = NSBitmapImageRep(data: img.tiffRepresentation!)!
let W = CGFloat(rep.pixelsWide), H = CGFloat(rep.pixelsHigh)
let tw = CGFloat(Double(a[3])!), scale = tw / W, ph = CGFloat(Double(a[4])!)
let th = H * scale
var y: CGFloat = 0, i = 0
while y < th {
    let h = min(ph, th - y)
    let out = NSImage(size: NSSize(width: tw, height: h))
    out.lockFocus()
    rep.draw(in: NSRect(x: 0, y: h - th + y, width: tw, height: th))
    out.unlockFocus()
    let r = NSBitmapImageRep(data: out.tiffRepresentation!)!
    try! r.representation(using: .jpeg, properties: [.compressionFactor: 0.8])!.write(to: URL(fileURLWithPath: "\(a[2])-\(i).jpg"))
    y += ph; i += 1
}
print(i)
