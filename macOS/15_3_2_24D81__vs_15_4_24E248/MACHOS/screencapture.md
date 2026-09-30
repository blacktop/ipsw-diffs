## screencapture

> `/usr/sbin/screencapture`

```diff

-331.3.1.0.0
-  __TEXT.__text: 0x6d4f0
-  __TEXT.__auth_stubs: 0x3620
-  __TEXT.__objc_methlist: 0x18c
-  __TEXT.__const: 0x3cac
-  __TEXT.__cstring: 0x30cc
-  __TEXT.__swift5_typeref: 0x138e
+331.4.4.0.0
+  __TEXT.__text: 0x6bf14
+  __TEXT.__auth_stubs: 0x3660
+  __TEXT.__objc_methlist: 0x428
+  __TEXT.__const: 0x3c8c
+  __TEXT.__cstring: 0x2bfc
+  __TEXT.__swift5_typeref: 0x137e
   __TEXT.__swift5_capture: 0x7c8
   __TEXT.__objc_methname: 0x116f
   __TEXT.__oslogstring: 0xa61
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x1680
+  __TEXT.__constg_swiftt: 0x1650
   __TEXT.__swift5_builtin: 0x12c
-  __TEXT.__swift5_reflstr: 0x15fb
-  __TEXT.__swift5_fieldmd: 0x1a58
+  __TEXT.__swift5_reflstr: 0x15eb
+  __TEXT.__swift5_fieldmd: 0x1a18
   __TEXT.__swift5_assocty: 0x628
   __TEXT.__swift5_proto: 0x330
-  __TEXT.__swift5_types: 0x23c
+  __TEXT.__swift5_types: 0x238
   __TEXT.__objc_classname: 0xf5
   __TEXT.__objc_methtype: 0x330
+  __TEXT.__swift_as_entry: 0x64
+  __TEXT.__swift_as_ret: 0x6c
   __TEXT.__swift5_protos: 0x3c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x2320
-  __TEXT.__eh_frame: 0x1694
-  __DATA_CONST.__auth_got: 0x1b10
-  __DATA_CONST.__got: 0x7c0
-  __DATA_CONST.__auth_ptr: 0x8a8
-  __DATA_CONST.__const: 0x5298
+  __TEXT.__unwind_info: 0x22d0
+  __TEXT.__eh_frame: 0x1738
+  __DATA_CONST.__auth_got: 0x1b30
+  __DATA_CONST.__got: 0x740
+  __DATA_CONST.__auth_ptr: 0x860
+  __DATA_CONST.__const: 0x5260
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA.__objc_const: 0x15c0
-  __DATA.__objc_selrefs: 0x5c0
-  __DATA.__objc_data: 0x560
-  __DATA.__data: 0x16c8
-  __DATA.__common: 0x408
-  __DATA.__bss: 0x4698
+  __DATA.__objc_const: 0x1200
+  __DATA.__objc_selrefs: 0x690
+  __DATA.__objc_data: 0x490
+  __DATA.__data: 0x1668
+  __DATA.__common: 0x3f0
+  __DATA.__bss: 0x4678
   _TEXT.crosshair.png: 0x47a
   _TEXT.crosshair@2x.png: 0x715
   _TEXT.shadow.png: 0xe4c

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 5EFF42C5-384D-3E79-B23A-2BDA723F566D
-  Functions: 3682
-  Symbols:   1285
-  CStrings:  656
+  UUID: E1D0711E-30C6-3E37-8EC6-0B0E2E81D6B6
+  Functions: 3679
+  Symbols:   1281
+  CStrings:  630
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftDataDetection
- _$sSa12_endMutationyyFyXl_Ts5
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
CStrings:
+ "com.apple.MobileSMS"
+ "usage: screencapture [-icMPmwsWxSCUtoa] [files]\n  -c         force screen capture to go to the clipboard\n  -b         capture Touch Bar - non-interactive modes only\n  -C         capture the cursor as well as the screen. only in non-interactive modes\n  -d         display errors to the user graphically\n  -i         capture screen interactively, by selection or window\n               control key - causes screenshot to go to clipboard\n               space key   - toggle between mouse selection and\n                             window selection modes\n               escape key  - cancels interactive screenshot\n  -m         only capture the main monitor, undefined if -i is set\n  -D<display> screen capture or record from the display specified. -D 1 is main display, -D 2 secondary, etc.\n  -o         in window capture mode, do not capture the shadow of the window\n  -p         screen capture will use the default settings for capture. The files argument will be ignored\n  -M         screen capture output will go to a new Mail message\n  -P         screen capture output will open in Preview or QuickTime Player if video\n  -B<bundleid> screen capture output will open in app with bundleid\n  -s         only allow mouse selection mode\n  -S         in window capture mode, capture the screen not the window\n  -J<style>  sets the starting of interactive capture\n               selection       - captures screen in selection mode\n               window          - captures screen in window mode\n               video           - records screen in selection mode\n  -t<format> image format to create, default is png (other options include pdf, jpg, tiff and other formats)\n  -T<seconds> take the picture after a delay of <seconds>, default is 5\n  -w         only allow window selection mode\n  -W         start interaction in window selection mode\n  -x         do not play sounds\n  -a         do not include windows attached to selected windows\n  -r         do not add dpi meta data to image\n  -l<windowid> capture this windowsid\n  -R<x,y,w,h> capture screen rect\n  -v        capture video recording of the screen\n  -V<seconds> limits video capture to specified seconds\n  -g        captures audio during a video recording using default input.\n  -G<id>    captures audio during a video recording using audio id specified.\n  -k        show clicks in video recording mode\n  -U        Show interactive toolbar in interactive mode\n  -u        present UI after screencapture is complete. files passed to command line will be ignored\n  files   where to save the screen capture, 1 file per screen"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "Must take zero or more splits"
- "Negative value is not representable"
- "Not enough bits to represent the passed value"
- "Range requires lowerBound <= upperBound"
- "Swift/Array.swift"
- "Swift/Collection.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
- "Swift/Range.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "invalid Collection: less than 'count' elements in collection"
- "usage: screencapture [-icMPmwsWxSCUtoa] [files]\n  -c         force screen capture to go to the clipboard\n  -b         capture Touch Bar - non-interactive modes only\n  -C         capture the cursor as well as the screen. only in non-interactive modes\n  -d         display errors to the user graphically\n  -i         capture screen interactively, by selection or window\n               control key - causes screenshot to go to clipboard\n               space key   - toggle between mouse selection and\n                             window selection modes\n               escape key  - cancels interactive screenshot\n  -m         only capture the main monitor, undefined if -i is set\n  -D<display> screen capture or record from the display specified. -D 1 is main display, -D 2 secondary, etc.\n  -o         in window capture mode, do not capture the shadow of the window\n  -p         screen capture will use the default settings for capture. The files argument will be ignored\n  -M         screen capture output will go to a new Mail message\n  -P         screen capture output will open in Preview or QuickTime Player if video\n  -I         screen capture output will open in Messages\n  -B<bundleid> screen capture output will open in app with bundleid\n  -s         only allow mouse selection mode\n  -S         in window capture mode, capture the screen not the window\n  -J<style>  sets the starting of interfactive capture\n               selection       - captures screen in selection mode\n               window          - captures screen in window mode\n               video           - records screen in selection mode\n  -t<format> image format to create, default is png (other options include pdf, jpg, tiff and other formats)\n  -T<seconds> take the picture after a delay of <seconds>, default is 5\n  -w         only allow window selection mode\n  -W         start interaction in window selection mode\n  -x         do not play sounds\n  -a         do not include windows attached to selected windows\n  -r         do not add dpi meta data to image\n  -l<windowid> capture this windowsid\n  -R<x,y,w,h> capture screen rect\n  -v        capture video recording of the screen\n  -V<seconds> limits video capture to specified seconds\n  -g        captures audio during a video recording using default input.\n  -G<id>    captures audio during a video recording using audio id specified.\n  -k        show clicks in video recording mode\n  -U        Show interactive toolbar in interactive mode\n  -u        present UI after screencapture is complete. files passed to command line will be ignored\n  files   where to save the screen capture, 1 file per screen"

```
