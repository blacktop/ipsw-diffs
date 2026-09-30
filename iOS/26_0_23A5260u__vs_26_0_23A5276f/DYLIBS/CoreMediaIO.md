## CoreMediaIO

> `/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO`

```diff

-5610.0.0.0.0
-  __TEXT.__text: 0x46dd4
+5612.0.0.0.0
+  __TEXT.__text: 0x46c04
   __TEXT.__auth_stubs: 0xe30
   __TEXT.__objc_methlist: 0x2014
   __TEXT.__const: 0xe8
   __TEXT.__gcc_except_tab: 0x16b8
-  __TEXT.__cstring: 0x84e4
-  __TEXT.__oslogstring: 0x42ae
+  __TEXT.__cstring: 0x8505
+  __TEXT.__oslogstring: 0x4266
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__unwind_info: 0xca8
   __TEXT.__objc_classname: 0x3bf

   __TEXT.__objc_methtype: 0x10e4
   __TEXT.__objc_stubs: 0x3180
   __DATA_CONST.__got: 0x270
-  __DATA_CONST.__const: 0xd50
+  __DATA_CONST.__const: 0xd68
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0xd8
   __AUTH_CONST.__auth_got: 0x728
   __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0x20c0
+  __AUTH_CONST.__cfstring: 0x2120
   __AUTH_CONST.__objc_const: 0x39f0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x364

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0F15476B-3499-3643-B6C3-3027818F6845
+  UUID: 5F04BF68-90C1-3A50-93DD-F05583C480FD
   Functions: 1329
-  Symbols:   4398
-  CStrings:  2222
+  Symbols:   4375
+  CStrings:  2226
 
Symbols:
+ _CMIOExtensionPropertyStreamFaceTrackingFailureFieldOfViewModifier
+ _CMIOExtensionPropertyStreamFaceTrackingMaxFaces
+ _CMIOExtensionPropertyStreamFaceTrackingNetworkFailureThresholdMultiplier
Functions:
~ -[CMIOExtensionStream sendSampleBuffer:discontinuity:hostTimeInNanoseconds:] : 1464 -> 1484
~ -[CMIOExtensionProvider removeSystemStatusAttributionsForClient:stream:] : 488 -> 4
CStrings:
+ "FaceTrackingFailureFieldOfViewModifier"
+ "FaceTrackingMaxFaces"
+ "FaceTrackingNetworkFailureThresholdMultiplier"
- "%s:%d:%s removeSystemStatusAttributionsForClient for client %{private}d"
- "-[CMIOExtensionProvider removeSystemStatusAttributionsForClient:stream:]"

```
