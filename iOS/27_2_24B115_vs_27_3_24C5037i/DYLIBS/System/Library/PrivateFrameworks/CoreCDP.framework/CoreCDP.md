## CoreCDP

> `/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP`

```diff

-448.125.10.0.0
-  __TEXT.__text: 0x4e974
-  __TEXT.__objc_methlist: 0x3ab4
-  __TEXT.__const: 0x14d4
+448.250.2.0.0
+  __TEXT.__text: 0x4e9b8
+  __TEXT.__objc_methlist: 0x3ac4
+  __TEXT.__const: 0x14e4
   __TEXT.__gcc_except_tab: 0x1114
   __TEXT.__oslogstring: 0x91ef
-  __TEXT.__cstring: 0x66ba
+  __TEXT.__cstring: 0x6831
   __TEXT.__dlopen_cstrs: 0xca
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x2040
+  __TEXT.__unwind_info: 0x2048
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2ff8
+  __DATA_CONST.__const: 0x3020
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21e8
+  __DATA_CONST.__objc_selrefs: 0x21f0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xe8
-  __DATA_CONST.__objc_arraydata: 0x90
+  __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__got: 0x4f8
-  __AUTH_CONST.__const: 0x630
-  __AUTH_CONST.__cfstring: 0x3f80
-  __AUTH_CONST.__objc_const: 0x8868
+  __AUTH_CONST.__const: 0x650
+  __AUTH_CONST.__cfstring: 0x40e0
+  __AUTH_CONST.__objc_const: 0x8878
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x878
   __DATA.__objc_ivar: 0x300
-  __DATA.__data: 0x11a0
+  __DATA.__data: 0x11a8
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x1090
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2406
-  Symbols:   3908
-  CStrings:  1649
+  Functions: 2409
+  Symbols:   3920
+  CStrings:  1661
 
Symbols:
+ +[CDPUtilities isDBRServerRecreationEnabled]
+ _OBJC_CLASS_$_NSConstantArray
+ ___40+[CDPUtilities sanitizedInfoDictionary:]_block_invoke
+ ___der_key_expert_tbm_support
+ _der_key_expert_tbm_support
+ _kCDPAnalyticsPDPServerRecreationFinishEvent
+ _kCDPAnalyticsPDPServerRecreationSetupAfterRecreateEvent
+ _kCDPAnalyticsPDPServerRecreationSkippedEvent
+ _kCDPAnalyticsPDPServerRecreationStartEvent
+ _kCDPAnalyticsPDPSetupHealedOnRevalidateEvent
+ _sanitizedInfoDictionary:.onceToken
+ _sanitizedInfoDictionary:.sensitiveKeys
Functions:
+ +[CDPUtilities isDBRServerRecreationEnabled]
~ +[CDPUtilities sanitizedInfoDictionary:] : 452 -> 376
+ ___40+[CDPUtilities sanitizedInfoDictionary:]_block_invoke
+ _CDPLocalizedStringInTable.cold.1
~ _aks_drain_backup_keys_info : 292 -> 280
CStrings:
+ "DBRServerRecreation"
+ "DBRServerRecreationEnabled"
+ "com.apple.corecdp.pdpServerRecreationFinish"
+ "com.apple.corecdp.pdpServerRecreationSetupAfterRecreate"
+ "com.apple.corecdp.pdpServerRecreationSkipped"
+ "com.apple.corecdp.pdpServerRecreationStart"
+ "com.apple.corecdp.pdpSetupHealedOnRevalidate"
+ "isStoreDemoModeEnabled:"
+ "kPCSAuthenticateAppleID"
+ "kPCSSetupAltDSID"
+ "kPCSSetupAuthToken"
+ "kPCSSetupPassword"
+ "kPCSSetupUsername"
- "isSecureDemoModeEnabled:"
```
