## AppleUVDMLib

> `/System/Library/Extensions/AppleUVDM.kext/Contents/PlugIns/AppleUVDMLib.plugin/Contents/MacOS/AppleUVDMLib`

```diff

 24.0.0.0.0
-  __TEXT.__text: 0xd8c
+  __TEXT.__text: 0xd90
   __TEXT.__auth_stubs: 0x150
   __TEXT.__gcc_except_tab: 0x20
   __TEXT.__cstring: 0x12

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 8895C007-8CF6-3DC3-B753-32DFDB94BAA8
+  UUID: 65C960C8-E81B-31BD-ABF3-A0E023E9CD70
   Functions: 23
   Symbols:   55
   CStrings:  1
Functions:
~ __ZN16AppleUVDMLibPriv12openEndpointEPv : 76 -> 80
~ __ZN16AppleUVDMLibPriv13closeEndpointEPv : 76 -> 80
~ __ZN16AppleUVDMLibPriv10readStreamEPvytPtPhyh : 540 -> 536

```
