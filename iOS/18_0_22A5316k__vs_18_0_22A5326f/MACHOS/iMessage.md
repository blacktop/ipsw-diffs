## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1301.100.8.2.5
-  __TEXT.__text: 0x8fdc0
-  __TEXT.__auth_stubs: 0x1320
-  __TEXT.__objc_stubs: 0xaf40
-  __TEXT.__objc_methlist: 0x210c
+1303.100.13.0.0
+  __TEXT.__text: 0x905e0
+  __TEXT.__auth_stubs: 0x1330
+  __TEXT.__objc_stubs: 0xb000
+  __TEXT.__objc_methlist: 0x2124
   __TEXT.__const: 0x37e
-  __TEXT.__gcc_except_tab: 0xa5a4
-  __TEXT.__cstring: 0x2e8d
-  __TEXT.__oslogstring: 0x13ad6
-  __TEXT.__objc_classname: 0x4e5
-  __TEXT.__objc_methname: 0xff1a
-  __TEXT.__objc_methtype: 0x2776
+  __TEXT.__gcc_except_tab: 0xa620
+  __TEXT.__cstring: 0x2ead
+  __TEXT.__oslogstring: 0x13c06
+  __TEXT.__objc_classname: 0x4e4
+  __TEXT.__objc_methname: 0x10062
+  __TEXT.__objc_methtype: 0x2779
   __TEXT.__ustring: 0x4
   __TEXT.__constg_swiftt: 0x150
-  __TEXT.__swift5_typeref: 0x253
+  __TEXT.__swift5_typeref: 0x251
   __TEXT.__swift5_reflstr: 0x1f
   __TEXT.__swift5_fieldmd: 0x48
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_capture: 0xa0
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1d60
+  __TEXT.__unwind_info: 0x1d78
   __TEXT.__eh_frame: 0x2b8
-  __DATA_CONST.__auth_got: 0x9a0
-  __DATA_CONST.__got: 0xd70
+  __DATA_CONST.__auth_got: 0x9a8
+  __DATA_CONST.__got: 0xd68
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x29b0
-  __DATA_CONST.__cfstring: 0x31a0
+  __DATA_CONST.__const: 0x2ab8
+  __DATA_CONST.__cfstring: 0x31e0
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x3560
-  __DATA.__objc_selrefs: 0x3108
-  __DATA.__objc_ivar: 0x1b0
+  __DATA.__objc_const: 0x3590
+  __DATA.__objc_selrefs: 0x3138
+  __DATA.__objc_ivar: 0x1b4
   __DATA.__objc_data: 0x378
   __DATA.__data: 0x770
   __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0x500
-  __DATA_DIRTY.__data: 0xc
+  __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1160
-  Symbols:   757
-  CStrings:  4117
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 1162
+  Symbols:   765
+  CStrings:  4134
 
Symbols:
+ _IMStickerTransferInfoDirectoryURL
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _kStickerTransferInfoPlistFileFolder
CStrings:
+ "!"
+ "%!{(MISSING)public}s alias %!s(MISSING) SIMID %!s(MISSING) no longer a valid subscription, defaulting to whether iMessage is available"
+ "@48@0:8@16B24I28B32B36B40B44"
+ "Appending off grid status of %!@(MISSING) for handle ID %!@(MISSING) "
+ "Attempting to append off grid status to message dictionary"
+ "Missing identifier for this off grid status payload!"
+ "No participant found, not appending off grid status"
+ "Not appending off grid status, not a 1:1 chat"
+ "TB,R,N,V_isBackwardsCompatibleMessage"
+ "_appendSeenOffGridStatusToMessageDictionary:forChat:"
+ "_isBackwardsCompatibleMessage"
+ "cachedOffGridModeAndLastPublisherWithCompletion:"
+ "didReceiveOffGridStatus:forID:messageGUID:account:"
+ "initWithDisplayIDs:didSucceed:error:isFromMeToMe:shouldDeactivate:destinationIsOffGrid:isBackwardsCompatibleMessage:"
+ "isBackwardsCompatibleMessage"
+ "isBackwardsCompatibleMessage %!@(MISSING)"
+ "messageSummaryInfoForSending"
+ "setBackwardsCompatibleVersion:"
+ "setExpectedOffGridCapableDeliveries:"
+ "sofg"
+ "sofgid"
+ "v20@?0B8@\"NSData\"12"
+ "v36@?0@\"MessageDeliveryController\"8@\"NSArray\"16B24I28B32"
- "?0"
- "@44@0:8@16B24I28B32B36B40"
- "Message %!@(MISSING) was sent to a user that is off grid using regular iMessage, offer send via satellite"
- "didReceiveOffGridStatus:forMessageGUID:account:"
- "initWithDisplayIDs:didSucceed:error:isFromMeToMe:shouldDeactivate:destinationIsOffGrid:"
- "v32@?0@\"MessageDeliveryController\"8@\"NSArray\"16B24I28"

```
