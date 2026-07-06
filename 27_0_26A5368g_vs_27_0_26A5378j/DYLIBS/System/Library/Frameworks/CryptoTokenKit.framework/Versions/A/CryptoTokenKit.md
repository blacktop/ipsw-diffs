## CryptoTokenKit

> `/System/Library/Frameworks/CryptoTokenKit.framework/Versions/A/CryptoTokenKit`

```diff

-  __TEXT.__text: 0x72fd4
+  __TEXT.__text: 0x73a94
   __TEXT.__delay_helper: 0x1f0
   __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_methlist: 0x55a8
+  __TEXT.__objc_methlist: 0x55b8
   __TEXT.__const: 0x7d1
-  __TEXT.__cstring: 0x3bce
-  __TEXT.__oslogstring: 0x7303
-  __TEXT.__gcc_except_tab: 0x1438
+  __TEXT.__cstring: 0x3c0e
+  __TEXT.__oslogstring: 0x7433
+  __TEXT.__gcc_except_tab: 0x1510
   __TEXT.__swift5_typeref: 0x2a9
   __TEXT.__swift5_capture: 0x310
   __TEXT.__constg_swiftt: 0x2d4

   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x1e40
+  __TEXT.__unwind_info: 0x1e78
   __TEXT.__eh_frame: 0x738
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a90
+  __DATA_CONST.__objc_selrefs: 0x2ac0
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x2b8
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0x7b8
-  __AUTH_CONST.__const: 0x2d08
-  __AUTH_CONST.__cfstring: 0x3ce0
-  __AUTH_CONST.__objc_const: 0x9a70
+  __DATA_CONST.__got: 0x7d0
+  __AUTH_CONST.__const: 0x2d88
+  __AUTH_CONST.__cfstring: 0x3d00
+  __AUTH_CONST.__objc_const: 0x9a80
   __AUTH_CONST.__lazy_load_got: 0x8
   __AUTH_CONST.__objc_intobj: 0x5e8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0xc10
-  __AUTH.__objc_data: 0x9a0
+  __AUTH.__objc_data: 0x15a8
   __AUTH.__data: 0x240
   __DATA.__objc_ivar: 0x5e8
   __DATA.__data: 0xf08
-  __DATA.__bss: 0x880
+  __DATA.__bss: 0x890
   __DATA.__common: 0x28
-  __DATA_DIRTY.__objc_data: 0x1978
+  __DATA_DIRTY.__objc_data: 0xd70
   __DATA_DIRTY.__data: 0x4
-  __DATA_DIRTY.__bss: 0x2b0
+  __DATA_DIRTY.__bss: 0x2a8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2937
-  Symbols:   6348
-  CStrings:  1812
+  Functions: 2947
+  Symbols:   6374
+  CStrings:  1821
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__lazy_load_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Symbols:
+ +[TKLoginHelper pairWithExpiredCertificatesPrefKey]
+ -[TKSmartCardSlotEngine clientConnectionTerminated:]
+ GCC_except_table60
+ GCC_except_table75
+ GCC_except_table85
+ GCC_except_table95
+ GCC_except_table97
+ _OBJC_CLASS_$_NSMutableIndexSet
+ _OUTLINED_FUNCTION_48
+ _OUTLINED_FUNCTION_55
+ _OUTLINED_FUNCTION_60
+ _OUTLINED_FUNCTION_66
+ ___49+[TKLoginHelper getSmartcardSettingResultWorker:]_block_invoke
+ ___52-[TKSmartCardSlotEngine clientConnectionTerminated:]_block_invoke
+ ___60-[TKSmartCardSlotEngine listener:shouldAcceptNewConnection:]_block_invoke
+ ___60-[TKSmartCardSlotEngine listener:shouldAcceptNewConnection:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40s_e42_v32?0"TKSmartCardSessionRequest"8Q16^B24l
+ ___block_descriptor_48_e8_32w40w_e5_v8?0l
+ ___copy_helper_block_e8_32w40w
+ ___destroy_helper_block_e8_32w40w
+ _objc_msgSend$addIndex:
+ _objc_msgSend$clientConnectionTerminated:
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$indexSet
+ _objc_msgSend$pairWithExpiredCertificatesPrefKey
+ _objc_msgSend$removeObjectsAtIndexes:
+ getSmartcardSettingResultWorker:.machineOnlyKeys
+ getSmartcardSettingResultWorker:.machineOnlyKeysOnce
- GCC_except_table51
- GCC_except_table56
- GCC_except_table79
- GCC_except_table91
- _OUTLINED_FUNCTION_47
- _OUTLINED_FUNCTION_50
- _OUTLINED_FUNCTION_56
- _OUTLINED_FUNCTION_61
CStrings:
+ "%{public}@: client pid %d gone while holding the session, reclaiming it"
+ "%{public}@: client pid %d gone, dropping %lu queued session request(s)"
+ "%{public}@: clientConnectionTerminated for pid %d"
+ "%{public}@: session busy (held by pid %d), pid %d queued behind it (%lu waiting); notifying holder"
+ "%{public}@: session granted to pid %d (%lu still waiting)"
+ "%{public}@: session requested by pid %d (%lu now queued)"
+ "%{public}@: state reply for client with no pending request, ignoring"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "PairWithExpiredCertificates"
+ "v32@?0@\"TKSmartCardSessionRequest\"8Q16^B24"
- "%{public}@: notifyWithParameters reply for client with no state request — request was torn down or replaced mid-flight (waitForStateFlushedWithReply may stall)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6yKJWu/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6yKJWu/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6yKJWu/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"

```
