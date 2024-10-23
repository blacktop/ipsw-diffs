## libBasebandCommandDriversARI.dylib

> `/usr/lib/libBasebandCommandDriversARI.dylib`

```diff

-1183.0.0.0.0
-  __TEXT.__text: 0xa1c1c
-  __TEXT.__auth_stubs: 0x2da0
-  __TEXT.__init_offsets: 0xc
-  __TEXT.__cstring: 0x2ce7
-  __TEXT.__gcc_except_tab: 0xdb88
-  __TEXT.__const: 0x8048
-  __TEXT.__oslogstring: 0x1da6
-  __TEXT.__unwind_info: 0x39a0
+1209.0.0.0.0
+  __TEXT.__text: 0xa26c0
+  __TEXT.__auth_stubs: 0x2df0
+  __TEXT.__init_offsets: 0x10
+  __TEXT.__cstring: 0x2d89
+  __TEXT.__gcc_except_tab: 0xdda4
+  __TEXT.__const: 0x8090
+  __TEXT.__oslogstring: 0x1db3
+  __TEXT.__unwind_info: 0x39c0
   __DATA_CONST.__got: 0x678
-  __DATA_CONST.__const: 0x1080
+  __DATA_CONST.__const: 0x1088
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x16d8
+  __AUTH_CONST.__auth_got: 0x1700
   __AUTH_CONST.__const: 0x6b40
   __AUTH_CONST.__cfstring: 0xa0
-  __DATA.__data: 0x1a0
+  __DATA.__data: 0x1f0
+  __DATA.__bss: 0x20
   __DATA_DIRTY.__data: 0xa0
-  __DATA_DIRTY.__bss: 0x100
+  __DATA_DIRTY.__bss: 0xe8
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2115
-  Symbols:   3405
-  CStrings:  698
+  Functions: 2119
+  Symbols:   3418
+  CStrings:  702
 
Symbols:
+ _CFBooleanGetTypeID
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyBasebandWatchdogStop
+ __ZN12capabilities3abs27kKeySupportsCMHandDetectionE
+ __ZN3abm26kKeyTraceResetModeOnAPBootE
+ __ZN3abm8asStringENS_22ResetTraceModeOnAPBootE
+ __ZN3ctu2cf6assignERbPK11__CFBoolean
+ __ZN5radio16ARICommandDriver16getScrtPubK_syncEN3xpc4dictEN8dispatch8callbackIU13block_pointerFvNS1_6objectES5_EEE
+ __ZNSt3__118condition_variable10notify_allEv
+ __ZNSt3__118condition_variable15__do_timed_waitERNS_11unique_lockINS_5mutexEEENS_6chrono10time_pointINS5_12system_clockENS5_8durationIxNS_5ratioILl1ELl1000000000EEEEEEE
+ __ZNSt3__118condition_variableD1Ev
+ __ZNSt3__16chrono12steady_clock3nowEv
+ __ZNSt3__16chrono12system_clock3nowEv
- __ZN5radio16ARICommandDriver16getScrtPubK_syncEN3xpc4dictE
- _dispatch_group_wait
- _dispatch_time
CStrings:
+ "#I [ind] Trace output idle indication Success"
+ "#I [rsp] Succeeded to send trace config: %!s(MISSING)"
+ "/AppleInternal/Library/BuildRoots/be5905ba-8b8c-11ef-a962-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "/private/var/wireless/Library/Preferences/com.apple.AppleBasebandManager.Statistics.plist"
+ "AppleBasebandManager-AppleBasebandServices_Manager-1209"
+ "Error while waiting for trace output idle indication"
+ "Last_Used"
+ "Reset_Mode_Boot"
+ "Watchdog timed out"
+ "[ind] Error while unpacking trace output idle indication"
+ "[ind] Got unexpected message 0x%!x(MISSING), expected trace output idle indication (0x%!x(MISSING))"
+ "[rsp] Failed to send trace config!"
+ "[rsp] Failed to send trace config: unpackResult = %!d(MISSING) result_code_t1 = %!d(MISSING)"
- "#I Succeeded to send trace config: %!s(MISSING)"
- "#I Trace output idle indication Success"
- "/AppleInternal/Library/BuildRoots/b4a7daee-7dd0-11ef-a7b2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
- "AppleBasebandManager-AppleBasebandServices_Manager-1183"
- "Error while unpacking trace output idle indication"
- "Failed to send trace config!"
- "Failed to send trace config: unpackResult = %!d(MISSING) result_code_t1 = %!d(MISSING)"
- "Got unexpected message 0x%!x(MISSING), expected trace output idle indication (0x%!x(MISSING))"
- "Timeout waiting for trace output idle indication"

```
