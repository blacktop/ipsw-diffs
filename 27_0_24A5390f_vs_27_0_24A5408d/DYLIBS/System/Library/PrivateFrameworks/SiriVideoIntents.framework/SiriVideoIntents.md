## SiriVideoIntents

> `/System/Library/PrivateFrameworks/SiriVideoIntents.framework/SiriVideoIntents`

```diff

-3600.28.6.0.0
-  __TEXT.__text: 0x1c6574
+3600.28.7.0.0
+  __TEXT.__text: 0x1c71bc
   __TEXT.__objc_methlist: 0x12b0
-  __TEXT.__const: 0x150e0
-  __TEXT.__oslogstring: 0xdfd7
+  __TEXT.__const: 0x15170
+  __TEXT.__oslogstring: 0xe19d
   __TEXT.__cstring: 0x5756
-  __TEXT.__constg_swiftt: 0x6c50
-  __TEXT.__swift5_typeref: 0x638a
-  __TEXT.__swift5_fieldmd: 0x6368
+  __TEXT.__constg_swiftt: 0x6cb4
+  __TEXT.__swift5_typeref: 0x63da
+  __TEXT.__swift5_reflstr: 0x5c30
+  __TEXT.__swift5_fieldmd: 0x6394
   __TEXT.__swift5_builtin: 0x21c
-  __TEXT.__swift5_reflstr: 0x5c17
   __TEXT.__swift5_assocty: 0xee8
   __TEXT.__swift5_capture: 0x2e5c
-  __TEXT.__swift5_proto: 0xd3c
-  __TEXT.__swift5_types: 0x688
-  __TEXT.__swift5_protos: 0x108
-  __TEXT.__swift_as_entry: 0x82c
-  __TEXT.__swift_as_ret: 0x94c
-  __TEXT.__swift_as_cont: 0xab4
+  __TEXT.__swift5_proto: 0xd40
+  __TEXT.__swift5_types: 0x68c
+  __TEXT.__swift5_protos: 0x10c
+  __TEXT.__swift_as_entry: 0x830
+  __TEXT.__swift_as_ret: 0x954
+  __TEXT.__swift_as_cont: 0xac4
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x7960
-  __TEXT.__eh_frame: 0x105b8
+  __TEXT.__unwind_info: 0x79b8
+  __TEXT.__eh_frame: 0x106b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1c0
-  __DATA_CONST.__objc_classlist: 0x400
+  __DATA_CONST.__objc_classlist: 0x408
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16d8
+  __DATA_CONST.__objc_selrefs: 0x1708
   __DATA_CONST.__objc_protorefs: 0xb8
-  __DATA_CONST.__got: 0x10a8
-  __AUTH_CONST.__const: 0x12028
-  __AUTH_CONST.__objc_const: 0xd838
+  __DATA_CONST.__got: 0x10b8
+  __AUTH_CONST.__const: 0x12060
+  __AUTH_CONST.__objc_const: 0xd8e8
   __AUTH_CONST.__auth_got: 0x2628
   __AUTH.__objc_data: 0x2850
-  __AUTH.__data: 0x6a28
-  __DATA.__data: 0x43d0
+  __AUTH.__data: 0x6ac8
+  __DATA.__data: 0x43b8
   __DATA.__bss: 0x17900
   __DATA.__common: 0x3a8
-  __DATA_DIRTY.__data: 0x2a0
+  __DATA_DIRTY.__data: 0x2b0
   __DATA_DIRTY.__common: 0x60
+  - /System/Library/Frameworks/AVRouting.framework/AVRouting
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11601
-  Symbols:   3988
-  CStrings:  1446
+  Functions: 11617
+  Symbols:   4003
+  CStrings:  1450
 
Symbols:
+ _OBJC_CLASS_$_AVOutputContext
+ _OBJC_CLASS_$_AVOutputDevice
+ __DATA__TtC16SiriVideoIntents26CarPlayVideoOutputProvider
+ __METACLASS_DATA__TtC16SiriVideoIntents26CarPlayVideoOutputProvider
+ ___unnamed_21
+ _objc_msgSend$deviceType
+ _objc_msgSend$isCarPlayVideoActive
+ _objc_msgSend$isCarPlayVideoAllowed
+ _objc_msgSend$outputDevices
+ _objc_msgSend$setCarPlayVideoActive:completionHandler:
+ _objc_msgSend$sharedSystemRemoteDisplayContext
+ _symbolic $s16SiriVideoIntents07CarPlayB15OutputProvidingP
+ _symbolic Sccyyt______pG s5ErrorP
+ _symbolic _____ 16SiriVideoIntents07CarPlayB14OutputProviderC
+ _symbolic ______p 16SiriVideoIntents07CarPlayB15OutputProvidingP
CStrings:
+ "CarPlayVideoOutputProvider.setCarPlayVideoActive() attempted to find CarPlay AVDevice, but none found"
+ "CarPlayVideoOutputProvider.setCarPlayVideoActive() attempted to set CarPlayActive, but not allowed in current state (e.g., user might be driving)"
+ "CarPlayVideoOutputProvider.setCarPlayVideoActive() failed to set CarPlay active: %s"
+ "CarPlayVideoOutputProvider.setCarPlayVideoActive() setting video active"
```
