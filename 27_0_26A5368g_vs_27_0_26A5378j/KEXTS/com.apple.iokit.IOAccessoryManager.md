## com.apple.iokit.IOAccessoryManager

> `com.apple.iokit.IOAccessoryManager`

```diff

   __TEXT.__const: 0x2b8
-  __TEXT.__cstring: 0x110ca
-  __TEXT.__os_log: 0x11fbd
-  __TEXT_EXEC.__text: 0xebaa0
+  __TEXT.__cstring: 0x110ec
+  __TEXT.__os_log: 0x12126
+  __TEXT_EXEC.__text: 0xebf28
   __TEXT_EXEC.__auth_stubs: 0xbc0
   __DATA.__data: 0x7e8
   __DATA.__common: 0x16b8
   __DATA.__bss: 0x142
   __DATA_CONST.__mod_init_func: 0x348
   __DATA_CONST.__mod_term_func: 0x340
-  __DATA_CONST.__const: 0x43220
+  __DATA_CONST.__const: 0x43268
   __DATA_CONST.__kalloc_type: 0x2500
   __DATA_CONST.__auth_got: 0x5e0
   __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__auth_ptr: 0x20
-  Functions: 5010
-  Symbols:   8234
-  CStrings:  2958
+  Functions: 5013
+  Symbols:   8243
+  CStrings:  2964
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Symbols:
+ __ZN17IOPortFeatureLDCM15setForcePortWetEb
+ __ZN27IOPortFeatureLDCMUserClient16_setForcePortWetEPS_PvP25IOExternalMethodArguments
+ __ZZN17IOPortFeatureLDCM15setForcePortWetEbE11_os_log_fmt
+ __ZZN17IOPortFeatureLDCM15setForcePortWetEbE11_os_log_fmt_0
+ __ZZN17IOPortFeatureLDCM21setMitigationsEnabledEbE11_os_log_fmt_4
+ __ZZN17IOPortFeatureLDCM31_portWetDryStateTransitionCheckEPKhmPbE11_os_log_fmt_3
+ __ZZN27IOPortFeatureLDCMUserClient16_setForcePortWetEPS_PvP25IOExternalMethodArgumentsE11_os_log_fmt
+ ____ZN17IOPortFeatureLDCM15setForcePortWetEb_block_invoke
CStrings:
+ "%s::%s(): Setting forcePortWet... (target: %s, forcePortWet: %s)\n"
+ "%s::%s(): [%s%s%s] ForcePortWet override active — treating measurement as wet\n\n"
+ "%s::%s(): [%s%s%s] LDCM: Empty port, no charger present - setting mitigations to Triggered\n\n"
+ "%s::%s(): [%s%s%s] LDCM: Empty port, was Failed - resetting to Triggered to dismiss intrusive UI\n\n"
+ "%s::%s(): [%s%s%s] forcePortWet: %s\n\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ieHQPG/Sources/IOAccessoryManager_Arrow/IOAccessoryIDBusTransport.cpp"
+ "1211111212221212111111211112112212122222222122121212"
+ "_setForcePortWet"
+ "setForcePortWet"
- "%s::%s(): [%s%s%s] Empty port, was Failed - resetting to Triggered to dismiss intrusive UI\n\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xDFCXr/Sources/IOAccessoryManager_Arrow/IOAccessoryIDBusTransport.cpp"
- "121111121222121211111121111211221212222222212212121"

```
