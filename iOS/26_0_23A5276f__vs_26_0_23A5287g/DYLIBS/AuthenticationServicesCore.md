## AuthenticationServicesCore

> `/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore`

```diff

-622.1.16.10.3
-  __TEXT.__text: 0xba2d4
+622.1.18.10.3
+  __TEXT.__text: 0xbadd8
   __TEXT.__auth_stubs: 0x2550
-  __TEXT.__objc_methlist: 0x36e0
-  __TEXT.__const: 0xbc98
-  __TEXT.__cstring: 0x4f42
-  __TEXT.__oslogstring: 0x3e90
+  __TEXT.__objc_methlist: 0x36f8
+  __TEXT.__const: 0xbcb8
+  __TEXT.__cstring: 0x4f72
+  __TEXT.__oslogstring: 0x3eb0
   __TEXT.__gcc_except_tab: 0x2e0
   __TEXT.__ustring: 0x564
   __TEXT.__dlopen_cstrs: 0x48
   __TEXT.__swift5_typeref: 0x2177
-  __TEXT.__constg_swiftt: 0x2380
-  __TEXT.__swift5_reflstr: 0x1601
-  __TEXT.__swift5_fieldmd: 0x213c
+  __TEXT.__constg_swiftt: 0x2388
+  __TEXT.__swift5_reflstr: 0x1621
+  __TEXT.__swift5_fieldmd: 0x2154
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_assocty: 0x3f0
   __TEXT.__swift5_proto: 0x92c
   __TEXT.__swift5_types: 0x29c
-  __TEXT.__swift5_capture: 0x458
+  __TEXT.__swift5_capture: 0x478
   __TEXT.__swift_as_entry: 0x70
   __TEXT.__swift_as_ret: 0x60
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x3220
-  __TEXT.__eh_frame: 0x4140
+  __TEXT.__unwind_info: 0x31c0
+  __TEXT.__eh_frame: 0x4190
   __TEXT.__objc_classname: 0x7a8
-  __TEXT.__objc_methname: 0xaa45
+  __TEXT.__objc_methname: 0xaafa
   __TEXT.__objc_methtype: 0x281c
-  __TEXT.__objc_stubs: 0x4480
-  __DATA_CONST.__got: 0x898
-  __DATA_CONST.__const: 0xb70
+  __TEXT.__objc_stubs: 0x44c0
+  __DATA_CONST.__got: 0x8a0
+  __DATA_CONST.__const: 0xba0
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c98
+  __DATA_CONST.__objc_selrefs: 0x1cb0
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x12b8
-  __AUTH_CONST.__const: 0x6110
-  __AUTH_CONST.__cfstring: 0x1ee0
-  __AUTH_CONST.__objc_const: 0x7670
+  __AUTH_CONST.__const: 0x6190
+  __AUTH_CONST.__cfstring: 0x1f20
+  __AUTH_CONST.__objc_const: 0x76c0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xbe0
   __AUTH.__data: 0x2e0
-  __DATA.__objc_ivar: 0x400
+  __DATA.__objc_ivar: 0x404
   __DATA.__data: 0x27d0
   __DATA.__bss: 0x11450
   __DATA.__common: 0x1d8
   __DATA_DIRTY.__objc_data: 0x1b70
-  __DATA_DIRTY.__data: 0x1088
+  __DATA_DIRTY.__data: 0x1098
   __DATA_DIRTY.__bss: 0xf20
   __DATA_DIRTY.__common: 0x88
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 97E4DF17-9D13-3FE3-8857-143CE32ACC5B
-  Functions: 4666
-  Symbols:   5259
-  CStrings:  2754
+  UUID: 3CF651FD-60AD-331C-A1DB-763AB5F66FBE
+  Functions: 4678
+  Symbols:   5272
+  CStrings:  2765
 
Symbols:
+ -[ASCAgent test_prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]
+ -[ASCAuthorizationPresentationContext isPasskeyRequest]
+ _ASCDigitalIdentityCredentialRequestTypeCredentialGet
+ _OBJC_IVAR_$_ASCAuthorizationPresentationContext._isPasskeyRequest
+ ___100-[ASCAgent test_prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke
+ ___100-[ASCAgent test_prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40bs_e49_v24?0"ASCCredentialRequestContext"8"NSError"16ls32l8s40l8
+ ___block_literal_global.136
+ ___block_literal_global.138
+ ___block_literal_global.143
+ ___block_literal_global.145
+ ___block_literal_global.387
+ ___block_literal_global.686
+ _objc_msgSend$updateLoginChoices:
+ _objc_msgSend$validatePresenceOfTestOptions:
- ___block_literal_global.130
- ___block_literal_global.135
- ___block_literal_global.137
- ___block_literal_global.142
- ___block_literal_global.380
- ___block_literal_global.685
- _objectdestroy.23Tm
CStrings:
+ "Cooldown %{public}s for %s aborted."
+ "Cooldown %{public}s for %s completed."
+ "Invalid JSON command, unexpected request type '%s'"
+ "Scheduling %{public}s cooldown for %s."
+ "TB,R,N,V_isPasskeyRequest"
+ "_isPasskeyRequest"
+ "credential.get"
+ "dc"
+ "isPasskeyRequest"
+ "maxBackoffShift"
+ "test_prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:"
+ "validatePresenceOfTestOptions:"
- "Cooldown for %s aborted."
- "Cooldown for %s completed."
- "Invalid JSON command, expected request type '%{public}s' but received '%s'"
- "Scheduling cooldown for %s."

```
