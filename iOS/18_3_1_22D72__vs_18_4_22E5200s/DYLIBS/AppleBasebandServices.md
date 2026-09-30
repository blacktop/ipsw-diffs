## AppleBasebandServices

> `/System/Library/PrivateFrameworks/AppleBasebandServices.framework/AppleBasebandServices`

```diff

-1220.0.0.0.0
-  __TEXT.__text: 0x19974
-  __TEXT.__auth_stubs: 0x770
-  __TEXT.__const: 0x55e
-  __TEXT.__gcc_except_tab: 0xbfc
-  __TEXT.__oslogstring: 0x199
-  __TEXT.__cstring: 0x2c0
-  __TEXT.__unwind_info: 0x618
+1245.0.0.0.0
+  __TEXT.__text: 0x18854
+  __TEXT.__auth_stubs: 0x840
+  __TEXT.__init_offsets: 0x4
+  __TEXT.__const: 0x647
+  __TEXT.__gcc_except_tab: 0xf0c
+  __TEXT.__oslogstring: 0x1c2
+  __TEXT.__cstring: 0x2f4
+  __TEXT.__unwind_info: 0x658
   __TEXT.__objc_methname: 0x1a
   __TEXT.__objc_stubs: 0x20
-  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__got: 0xd8
   __DATA_CONST.__const: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x3c8
-  __AUTH_CONST.__const: 0x790
-  __DATA.__data: 0x90
+  __AUTH_CONST.__auth_got: 0x430
+  __AUTH_CONST.__const: 0x7e0
+  __AUTH_CONST.__cfstring: 0x20
+  __DATA.__data: 0xe0
+  __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 266
-  Symbols:   439
-  CStrings:  62
+  Functions: 261
+  Symbols:   470
+  CStrings:  65
 
Symbols:
+ _CFBooleanGetTypeID
+ _CFGetTypeID
+ _CFRelease
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyBasebandWatchdogStop
+ __ZGVN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZN12capabilities3abs27kKeySupportsCMHandDetectionE
+ __ZN3ctu2cf12MakeCFStringC1EPKc
+ __ZN3ctu2cf12MakeCFStringD1Ev
+ __ZN3ctu2cf13plist_adapterC1EPK10__CFStringS4_
+ __ZN3ctu2cf13plist_adapterD1Ev
+ __ZN3ctu2cf6assignERbPK11__CFBoolean
+ __ZN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ ___CFConstantStringClassReference
+ __os_log_debug_impl
+ _kCFPreferencesCurrentUser
+ _pthread_mutex_lock
+ _pthread_mutex_unlock
CStrings:
+ "AppleBasebandManager-AppleBasebandServices_Manager-1245"
+ "Capability %s returning overridden value"
+ "Watchdog timed out"
+ "com.apple.telephony.capabilities"
- "AppleBasebandManager-AppleBasebandServices_Manager-1220"

```
