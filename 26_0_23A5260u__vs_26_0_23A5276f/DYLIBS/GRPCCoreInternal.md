## GRPCCoreInternal

> `/System/Library/PrivateFrameworks/GRPCCoreInternal.framework/GRPCCoreInternal`

```diff

-2.1.2.2.0
-  __TEXT.__text: 0x85a1c
-  __TEXT.__auth_stubs: 0x12c0
-  __TEXT.__swift5_typeref: 0x1a80
-  __TEXT.__const: 0x6b28
+2.1.2.200.0
+  __TEXT.__text: 0x855cc
+  __TEXT.__auth_stubs: 0x12d0
+  __TEXT.__swift5_typeref: 0x1adc
+  __TEXT.__const: 0x6b88
   __TEXT.__swift5_capture: 0x8ac
-  __TEXT.__constg_swiftt: 0x211c
-  __TEXT.__swift5_reflstr: 0x1151
-  __TEXT.__swift5_fieldmd: 0x1cd8
+  __TEXT.__constg_swiftt: 0x2134
+  __TEXT.__swift5_reflstr: 0x1171
+  __TEXT.__swift5_fieldmd: 0x1cf4
   __TEXT.__swift5_proto: 0x3b4
   __TEXT.__swift5_types: 0x29c
   __TEXT.__swift_as_entry: 0x2e0
   __TEXT.__swift5_assocty: 0x6b8
-  __TEXT.__swift5_protos: 0x2c
-  __TEXT.__cstring: 0x1147
+  __TEXT.__swift5_protos: 0x30
+  __TEXT.__cstring: 0x11d7
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_mpenum: 0x30
   __TEXT.__swift_as_ret: 0x348
-  __TEXT.__unwind_info: 0x2a70
-  __TEXT.__eh_frame: 0x5be4
+  __TEXT.__unwind_info: 0x2a68
+  __TEXT.__eh_frame: 0x5c2c
   __DATA_CONST.__got: 0x320
-  __DATA_CONST.__const: 0x1f0
+  __DATA_CONST.__const: 0x1d0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x960
-  __AUTH_CONST.__const: 0x6e70
+  __AUTH_CONST.__auth_got: 0x968
+  __AUTH_CONST.__const: 0x6e78
   __AUTH_CONST.__objc_const: 0x3f0
   __AUTH.__data: 0x518
-  __DATA.__data: 0x690
+  __DATA.__data: 0x6b0
   __DATA.__bss: 0xa4b0
   __DATA.__common: 0x10
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
-  UUID: E51EF489-57E2-3901-932F-550B20C3308E
+  UUID: 84251571-F4A8-317D-96C9-A6C908435A5E
   Functions: 3385
   Symbols:   973
   CStrings:  103
Symbols:
+ ___swift_memcpy112_8
+ _get_enum_tag_for_layout_string 16GRPCCoreInternal13ServerContextV17TransportSpecific_pSg
+ _symbolic $s16GRPCCoreInternal13ServerContextV17TransportSpecificP
+ _symbolic Say_____G 16GRPCCoreInternal6Base64O15DecodingOptionsV
+ _symbolic ______pSg 16GRPCCoreInternal13ServerContextV17TransportSpecificP
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 16GRPCCoreInternal6Base64O15DecodingOptionsV
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_GRPCCoreInternal
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_GRPCCoreInternal
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_GRPCCoreInternal
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_GRPCCoreInternal
CStrings:
+ "Can't call 'runConnections()' as the client is stopped (or is stopping). This can happen if the you call 'runConnections()' after shutting the client down or if you used 'withGRPCClient' with an empty body."
- "The client has stopped and can only be started once."

```
