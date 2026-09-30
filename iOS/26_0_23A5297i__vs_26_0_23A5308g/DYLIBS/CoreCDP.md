## CoreCDP

> `/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP`

```diff

-410.1.0.0.0
-  __TEXT.__text: 0x53408
-  __TEXT.__auth_stubs: 0x10a0
-  __TEXT.__objc_methlist: 0x3a54
+412.0.0.0.0
+  __TEXT.__text: 0x5395c
+  __TEXT.__auth_stubs: 0x10b0
+  __TEXT.__objc_methlist: 0x3a8c
   __TEXT.__const: 0x12e4
   __TEXT.__gcc_except_tab: 0x129c
-  __TEXT.__oslogstring: 0x8e89
-  __TEXT.__cstring: 0x600f
+  __TEXT.__oslogstring: 0x9046
+  __TEXT.__cstring: 0x6082
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x1568
+  __TEXT.__unwind_info: 0x1580
   __TEXT.__objc_classname: 0x71f
-  __TEXT.__objc_methname: 0x9229
-  __TEXT.__objc_methtype: 0x1c86
-  __TEXT.__objc_stubs: 0x4fe0
+  __TEXT.__objc_methname: 0x9343
+  __TEXT.__objc_methtype: 0x1c8e
+  __TEXT.__objc_stubs: 0x5020
   __DATA_CONST.__got: 0x4c8
-  __DATA_CONST.__const: 0x2f48
+  __DATA_CONST.__const: 0x2f70
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2158
+  __DATA_CONST.__objc_selrefs: 0x2190
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0x860
+  __AUTH_CONST.__auth_got: 0x868
   __AUTH_CONST.__const: 0x5d0
-  __AUTH_CONST.__cfstring: 0x3e80
-  __AUTH_CONST.__objc_const: 0x8ab0
+  __AUTH_CONST.__cfstring: 0x3f00
+  __AUTH_CONST.__objc_const: 0x8ae0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x820
-  __DATA.__objc_ivar: 0x300
+  __AUTH.__objc_data: 0x6e0
+  __DATA.__objc_ivar: 0x304
   __DATA.__data: 0x1100
   __DATA.__bss: 0x101
   __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0x870
+  __DATA_DIRTY.__objc_data: 0x9b0
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x118
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E499D233-FF13-3A38-9F36-8B712B1A5C0B
-  Functions: 2306
-  Symbols:   7675
-  CStrings:  3828
+  UUID: B6E1112A-CBB3-3385-A9E1-EC54FA99E66F
+  Functions: 2317
+  Symbols:   7706
+  CStrings:  3851
 
Symbols:
+ +[CDPUtilities fetchRPDProbationDurationConfigsWithCompletion:]
+ +[CDPUtilities isManateeNotificationOnFirstUnlockEnabledUsingURLBag:completion:]
+ +[CDPUtilities readPreferencesFor:].cold.1
+ -[CDPLocalDevice currentLockState]
+ -[CDPRecoveryFlowContext hasViableICSC]
+ -[CDPRecoveryFlowContext setHasViableICSC:]
+ _MKBGetDeviceLockState
+ _OBJC_IVAR_$_CDPRecoveryFlowContext._hasViableICSC
+ ___63+[CDPUtilities fetchRPDProbationDurationConfigsWithCompletion:]_block_invoke
+ ___80+[CDPUtilities isManateeNotificationOnFirstUnlockEnabledUsingURLBag:completion:]_block_invoke
+ ___80+[CDPUtilities isManateeNotificationOnFirstUnlockEnabledUsingURLBag:completion:]_block_invoke.cold.1
+ ___80+[CDPUtilities isManateeNotificationOnFirstUnlockEnabledUsingURLBag:completion:]_block_invoke.cold.2
+ ___80+[CDPUtilities isManateeNotificationOnFirstUnlockEnabledUsingURLBag:completion:]_block_invoke.cold.3
+ ___block_descriptor_40_e8_32bs_e20_v24?08"NSError"16ls32l8
+ ___block_literal_global.130
+ ___block_literal_global.189
+ ___block_literal_global.71
+ ___block_literal_global.77
+ ___block_literal_global.79
+ ___block_literal_global.99
+ _objc_msgSend$configurationValueForKey:completion:
+ _objc_msgSend$configurationValueForKey:fromCache:completion:
- ___block_literal_global.128
- ___block_literal_global.175
- ___block_literal_global.68
- ___block_literal_global.74
- ___block_literal_global.76
- ___block_literal_global.83
CStrings:
+ "Failed to fetch manatee configuration value from URL bag. Assuming we should continue posting notification."
+ "ManateeNotificationFirstUnlockKillSwitch"
+ "No config value found for manatee configuration. Assuming we should continue posting notification"
+ "Preferences value for key %@ is %{BOOL}d"
+ "Received rpdProbationDurationConfigs = %{public}@, error: %{public}@"
+ "TB,N,V_hasViableICSC"
+ "Unexpected type found while fetching manatee configuration value from URL Bag. Assuming we should continue posting notification."
+ "_hasViableICSC"
+ "configurationValueForKey:completion:"
+ "configurationValueForKey:fromCache:completion:"
+ "currentLockState"
+ "disableManateeNotificationOnFirstUnlock"
+ "fetchRPDProbationDurationConfigsWithCompletion:"
+ "hasViableICSC"
+ "i16@0:8"
+ "isManateeNotificationOnFirstUnlockEnabledUsingURLBag:completion:"
+ "rpd-probation-cfgs"
+ "setHasViableICSC:"

```
