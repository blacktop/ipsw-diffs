## MCCFoundation

> `/System/Library/PrivateFrameworks/MCCFoundation.framework/Versions/A/MCCFoundation`

```diff

-2027.0.5.0.0
-  __TEXT.__text: 0xada4
+2027.1.2.0.0
+  __TEXT.__text: 0xb078
   __TEXT.__const: 0xbc0
   __TEXT.__swift5_typeref: 0x2be
   __TEXT.__cstring: 0x4b7

   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_proto: 0x90
   __TEXT.__swift5_types: 0x38
-  __TEXT.__oslogstring: 0x368
+  __TEXT.__oslogstring: 0x408
   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x2c
   __TEXT.__swift_as_cont: 0x5c
-  __TEXT.__unwind_info: 0x3c8
+  __TEXT.__unwind_info: 0x3c0
   __TEXT.__eh_frame: 0x600
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x118
+  __DATA_CONST.__objc_selrefs: 0x150
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x8d0
   __AUTH_CONST.__auth_got: 0x3f0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 306
-  Symbols:   1000
-  CStrings:  60
+  Functions: 307
+  Symbols:   1010
+  CStrings:  61
 
Symbols:
+ _$s13MCCFoundation20MCCNetworkControllerV18makeDefaultSessionSo12NSURLSessionCyFZ
+ _OBJC_CLASS_$_NSURLSession
+ _OBJC_CLASS_$_NSURLSessionConfiguration
+ _objc_msgSend$URLCache
+ _objc_msgSend$configuration
+ _objc_msgSend$defaultSessionConfiguration
+ _objc_msgSend$diskCapacity
+ _objc_msgSend$sessionWithConfiguration:
+ _objc_msgSend$setRequestCachePolicy:
+ _objc_msgSend$setURLCache:
CStrings:
+ "MCCNetworkController was given a session with a disk-backed URLCache attached; authenticated requests must not be cached. Falling back to a safe session."
```
