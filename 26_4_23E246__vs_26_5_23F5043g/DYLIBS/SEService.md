## SEService

> `/System/Library/PrivateFrameworks/SEService.framework/SEService`

```diff

-64.24.0.0.0
-  __TEXT.__text: 0xf3914
+65.2.1.0.0
+  __TEXT.__text: 0xf39c8
   __TEXT.__auth_stubs: 0x1c70
   __TEXT.__objc_methlist: 0x3a7c
   __TEXT.__const: 0x15cd0
-  __TEXT.__oslogstring: 0x23a7
+  __TEXT.__oslogstring: 0x2477
   __TEXT.__cstring: 0x8035
-  __TEXT.__gcc_except_tab: 0x1eec
+  __TEXT.__gcc_except_tab: 0x1ef0
   __TEXT.__dlopen_cstrs: 0x64
   __TEXT.__constg_swiftt: 0x3108
   __TEXT.__swift5_typeref: 0x3d6c

   __TEXT.__swift5_capture: 0x1c8
   __TEXT.__unwind_info: 0x4a50
   __TEXT.__eh_frame: 0x530c
-  __TEXT.__objc_classname: 0xcff
-  __TEXT.__objc_methname: 0x8b07
-  __TEXT.__objc_methtype: 0x2b37
+  __TEXT.__objc_classname: 0xd0f
+  __TEXT.__objc_methname: 0x8b17
+  __TEXT.__objc_methtype: 0x2b47
   __TEXT.__objc_stubs: 0x48a0
   __DATA_CONST.__got: 0x658
   __DATA_CONST.__const: 0x16a8

   __AUTH_CONST.__auth_got: 0xe48
   __AUTH_CONST.__const: 0x9060
   __AUTH_CONST.__cfstring: 0x4360
-  __AUTH_CONST.__objc_const: 0x7ec0
+  __AUTH_CONST.__objc_const: 0x7ee0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0x518
   __AUTH.__data: 0x220
-  __DATA.__objc_ivar: 0x378
+  __DATA.__objc_ivar: 0x37c
   __DATA.__data: 0x4268
   __DATA.__bss: 0x23240
   __DATA.__common: 0x70

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: F12298DA-4C9E-37E6-B7F9-3EE89CE85F27
+  UUID: 70EA603C-8EEA-3D95-AB5B-446702C1A90E
   Functions: 6413
-  Symbols:   6182
-  CStrings:  3375
+  Symbols:   6183
+  CStrings:  3378
 
Symbols:
+ _OBJC_IVAR_$_SESNFCAppSettingsContext._stableIdentifier
+ ___block_literal_global.51
+ ___block_literal_global.54
+ ___block_literal_global.93
- ___block_literal_global.50
- ___block_literal_global.53
- ___block_literal_global.92
Functions:
~ -[SESNFCAppSettingsContext initWithBundleId:onChange:] : 472 -> 512
~ -[SESNFCAppSettingsContext isDefaultAppEligibleForService:] : 1272 -> 1240
~ -[SESNFCAppSettingsContext getDefaultNFCApplication] : 404 -> 420
~ -[SESNFCAppSettingsContext invalidate] : 180 -> 196
~ -[SESNFCAppSettingsContext .cxx_destruct] : 104 -> 116
~ -[SESNFCAppSettingsContext appBasedKeyPathChangeHandler:ofObject:change:context:] : 2492 -> 2596
~ -[SESNFCAppSettingsContext centralizedKeyPathChangeHandler:ofObject:change:context:] : 1912 -> 1936
CStrings:
+ "@\"NSUUID\""
+ "Context with identifier %@ - Default app queried with bundle Id %@"
+ "Context with identifier %@ - Invalidating app settings context for bundle ID %@"
+ "Context with identifier %@ - Key %@ changed, firing on visibility change for bundle Id %@"
+ "Context with identifier %@, Key %@ changed, firing on visibility change for bundle Id %@"
+ "Successfully initialized app settings context for bundle ID %@, with stable identifier %@"
+ "_stableIdentifier"
- "Default app queried with bundle Id %@"
- "Invalidating app settings context for bundle ID %@"
- "Key %@ changed, firing on visibility change for bundle Id %@"
- "Successfully initialized app settings context for bundle ID %@"

```
