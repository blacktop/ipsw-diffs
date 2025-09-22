## AppleBasebandServices

> `/System/Library/PrivateFrameworks/AppleBasebandServices.framework/AppleBasebandServices`

```diff

-1391.0.0.0.0
-  __TEXT.__text: 0x18178
-  __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__const: 0x56e
-  __TEXT.__gcc_except_tab: 0xbfc
-  __TEXT.__oslogstring: 0x1ae
-  __TEXT.__cstring: 0x2c7
-  __TEXT.__unwind_info: 0x598
+1397.0.0.0.0
+  __TEXT.__text: 0x18af8
+  __TEXT.__auth_stubs: 0x7d0
+  __TEXT.__init_offsets: 0x4
+  __TEXT.__const: 0x647
+  __TEXT.__gcc_except_tab: 0xf08
+  __TEXT.__oslogstring: 0x1d7
+  __TEXT.__cstring: 0x2fb
+  __TEXT.__unwind_info: 0x618
   __TEXT.__objc_methname: 0x1a
   __TEXT.__objc_stubs: 0x20
-  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__got: 0xc8
   __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x388
-  __AUTH_CONST.__const: 0x780
-  __DATA.__data: 0x90
+  __AUTH_CONST.__auth_got: 0x3f8
+  __AUTH_CONST.__const: 0x7d0
+  __AUTH_CONST.__cfstring: 0x20
+  __DATA.__data: 0xe0
+  __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4B46C2FB-DA76-396A-9E9C-51704ADA1C96
-  Functions: 253
-  Symbols:   792
-  CStrings:  61
+  UUID: 69493B24-7E4C-33EA-BE32-429019EB0219
+  Functions: 261
+  Symbols:   845
+  CStrings:  65
 
Symbols:
+ GCC_except_table10
+ GCC_except_table16
+ GCC_except_table23
+ GCC_except_table26
+ GCC_except_table3
+ GCC_except_table30
+ GCC_except_table31
+ GCC_except_table5
+ _CFBooleanGetTypeID
+ _CFGetTypeID
+ _CFRelease
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyBasebandWatchdogStop
+ __ZGVN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZN12capabilities3abs27kKeySupportsCMHandDetectionE
+ __ZN3ctu23PthreadMutexGuardPolicyI21CapabilitiesOverridesED1Ev
+ __ZN3ctu2cf12MakeCFStringC1EPKc
+ __ZN3ctu2cf12MakeCFStringD1Ev
+ __ZN3ctu2cf13plist_adapterC1EPK10__CFStringS4_
+ __ZN3ctu2cf13plist_adapterD1Ev
+ __ZN3ctu2cf6assignERbPK11__CFBoolean
+ __ZN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZNKSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE13__get_deleterERKSt9type_info
+ __ZNSt3__110shared_ptrI21CapabilitiesOverridesED2B8ne200100Ev
+ __ZNSt3__110unique_ptrI21CapabilitiesOverridesNS_14default_deleteIS1_EEED2B8ne200100Ev
+ __ZNSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEED1Ev
+ __ZTINSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEEE
+ __ZTSNSt3__110shared_ptrI21CapabilitiesOverridesE27__shared_ptr_default_deleteIS1_S1_EE
+ __ZTSNSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEEE
+ __ZTVNSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEEE
+ ___CFConstantStringClassReference
+ ___cxa_atexit
+ ___cxx_global_var_init
+ __os_log_debug_impl
+ _kCFPreferencesCurrentUser
+ _pthread_mutex_lock
+ _pthread_mutex_unlock
Functions:
~ __ZN7support2fs11updateOwnerENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEjj : 1508 -> 1552
~ __ZN7support2fs5isDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 164 -> 92
~ __ZN7support2fs5chownERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEjj : 48 -> 140
~ __ZN7support2fs7readDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS1_6vectorIS7_NS5_IS7_EEEE : 432 -> 460
~ __ZN7support2fs8openFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEit : 52 -> 160
~ __ZN7support2fs9closeFileEi : 72 -> 156
~ __ZN7support2fs8copyFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_b : 1272 -> 1364
~ __ZN7support2fs8loadFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS1_6vectorIcS6_EE : 740 -> 820
~ __ZN7support2fs8loadFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS1_6vectorIhNS5_IhEEEE : 372 -> 464
~ __ZN7support2fs10fileExistsERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 84 -> 168
~ __ZN7support2fs20createUniqueFilenameENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 6188 -> 6144
~ __ZN7support2fs16createUniquePathENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 728 -> 720
~ __ZN7support2fs9createDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEtb : 716 -> 772
~ __ZN7support2fs6renameERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_ : 64 -> 144
~ __ZN7support2fs5chmodERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEt : 48 -> 156
~ __ZN7support2fs9removeDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 1476 -> 1512
~ __ZN7support2fs10removeFileERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 100 -> 148
~ __ZN7support2fs17removeDirContentsERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm : 1584 -> 1524
~ __ZN7support2fs13moveDirUniqueERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_ : 340 -> 292
~ __ZN7support2fs7lockDirERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 148 -> 212
~ __ZN7support2fs9unlockDirEi : 100 -> 184
~ __ZNK12Capabilities26isCMHandDetectionSupportedEv : 48 -> 972
+ __ZN3ctu23PthreadMutexGuardPolicyI21CapabilitiesOverridesED1Ev
CStrings:
+ "AppleBasebandManager-AppleBasebandServices_Manager-1397"
+ "Capability %s returning overridden value"
+ "Watchdog timed out"
+ "com.apple.telephony.capabilities"
- "AppleBasebandManager-AppleBasebandServices_Manager-1391"

```
