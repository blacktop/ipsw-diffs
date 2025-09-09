## libHSFilerDynamic.dylib

> `/usr/lib/libHSFilerDynamic.dylib`

```diff

 1391.0.0.0.0
-  __TEXT.__text: 0x2f980
-  __TEXT.__auth_stubs: 0xbc0
-  __TEXT.__init_offsets: 0x38
-  __TEXT.__const: 0x21e7
-  __TEXT.__gcc_except_tab: 0x2528
-  __TEXT.__cstring: 0x984
-  __TEXT.__oslogstring: 0x2743
-  __TEXT.__unwind_info: 0x1008
-  __DATA_CONST.__got: 0x128
+  __TEXT.__text: 0x32f5c
+  __TEXT.__auth_stubs: 0xc90
+  __TEXT.__init_offsets: 0x3c
+  __TEXT.__const: 0x233f
+  __TEXT.__gcc_except_tab: 0x277c
+  __TEXT.__cstring: 0x9ca
+  __TEXT.__oslogstring: 0x2b18
+  __TEXT.__unwind_info: 0x10e0
+  __DATA_CONST.__got: 0x148
   __DATA_CONST.__const: 0x5b0
-  __AUTH_CONST.__auth_got: 0x5e8
-  __AUTH_CONST.__const: 0x2020
+  __AUTH_CONST.__auth_got: 0x650
+  __AUTH_CONST.__const: 0x2100
+  __AUTH_CONST.__cfstring: 0x20
   __DATA.__data: 0x1d0
+  __DATA.__bss: 0xa0
   __DATA.__common: 0x60
-  __DATA.__bss: 0x30
   __DATA_DIRTY.__data: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AppleBasebandLink.framework/AppleBasebandLink
+  - /System/Library/PrivateFrameworks/AppleMipcRouter.framework/AppleMipcRouter
   - /usr/lib/libARI.dylib
   - /usr/lib/libBasebandSharedServices.dylib
   - /usr/lib/libIOACIPC.dylib
   - /usr/lib/libIOACIPCBB.dylib
   - /usr/lib/libKTLDynamic.dylib
+  - /usr/lib/libMIPCSdk.dylib
   - /usr/lib/libPCITransport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyBasebandDynamic.dylib
   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 69FBE48D-EFBA-302F-ACC3-DD0C33318FE4
-  Functions: 741
-  Symbols:   2104
-  CStrings:  339
+  UUID: A7D3BC04-0E81-381F-A1C4-2A0FD4D398B2
+  Functions: 785
+  Symbols:   2220
+  CStrings:  373
 
Symbols:
+ _CFGetTypeID
+ _CFNumberGetTypeID
+ _CFNumberGetValue
+ _IOObjectRelease
+ _IORegistryEntryCreateCFProperty
+ _IOServiceGetMatchingService
+ __ZN12capabilities5radio3dalEv
+ __ZN3ctu2cf11CFSharedRefIKvED2Ev
+ __ZN5boost8lockfree5queueIPN7support9transport11io_async_cbEJEE3popIS5_EEbRT_
+ __ZN5boost8lockfree5queueIPN7support9transport11io_async_cbEJEED2Ev
+ __ZN5boost8lockfree6detail14freelist_stackINS0_5queueIPN7support9transport11io_async_cbEJEE4nodeENS_9alignment17aligned_allocatorIS9_Lm64EEEED2Ev
+ __ZN5boost9alignment17aligned_allocatorINS_8lockfree5queueIPN7support9transport11io_async_cbEJEE4nodeELm64EE8allocateEmPKv
+ __ZN5boost9alignment6detail15throw_exceptionISt9bad_allocEEvRKT_
+ __ZN7support4perf11memory_poolINS_9transport11io_async_cbELm256EEC2Ev
+ __ZN7support9transport7airship10write_syncEPvm
+ __ZN7support9transport7airship12sGetIOSizeRxENS1_8protocolE
+ __ZN7support9transport7airship12sGetIOSizeTxENS1_8protocolE
+ __ZN7support9transport7airship21sGetIOServicePropertyENS1_8protocolEPK10__CFStringRy
+ __ZN7support9transport7airship27sGetCFStringRefFromProtocolENS1_8protocolE
+ __ZN7support9transport7airship4initEv
+ __ZN7support9transport7airship4readEPvm
+ __ZN7support9transport7airship4readEPvmPm
+ __ZN7support9transport7airship4stopEv
+ __ZN7support9transport7airship5startEv
+ __ZN7support9transport7airship5writeEPvm
+ __ZN7support9transport7airship6createENS1_8protocolEb
+ __ZN7support9transport7airship9read_syncEPvm
+ __ZN7support9transport7airshipC1ENS1_8protocolE
+ __ZN7support9transport7airshipC2ENS1_8protocolE
+ __ZN7support9transport7airshipD1Ev
+ __ZN7support9transport7airshipD2Ev
+ __ZN7support9transportL12getLogClientEv
+ __ZNK7support9transport7airship14get_io_size_rxEv
+ __ZNKSt3__110__function6__funcIZN7support9transport7airshipC1ENS4_8protocolEE3$_0NS_9allocatorIS6_EEFvvEE11target_typeEv
+ __ZNKSt3__110__function6__funcIZN7support9transport7airshipC1ENS4_8protocolEE3$_0NS_9allocatorIS6_EEFvvEE6targetERKSt9type_info
+ __ZNKSt3__110__function6__funcIZN7support9transport7airshipC1ENS4_8protocolEE3$_0NS_9allocatorIS6_EEFvvEE7__cloneEPNS0_6__baseIS9_EE
+ __ZNKSt3__110__function6__funcIZN7support9transport7airshipC1ENS4_8protocolEE3$_0NS_9allocatorIS6_EEFvvEE7__cloneEv
+ __ZNKSt9bad_alloc4whatEv
+ __ZNSt3__110__function6__funcIZN7support9transport7airshipC1ENS4_8protocolEE3$_0NS_9allocatorIS6_EEFvvEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN7support9transport7airshipC1ENS4_8protocolEE3$_0NS_9allocatorIS6_EEFvvEE7destroyEv
+ __ZNSt3__110__function6__funcIZN7support9transport7airshipC1ENS4_8protocolEE3$_0NS_9allocatorIS6_EEFvvEED0Ev
+ __ZNSt3__110__function6__funcIZN7support9transport7airshipC1ENS4_8protocolEE3$_0NS_9allocatorIS6_EEFvvEED1Ev
+ __ZNSt3__110__function6__funcIZN7support9transport7airshipC1ENS4_8protocolEE3$_0NS_9allocatorIS6_EEFvvEEclEv
+ __ZNSt3__110unique_ptrIN7support9transport7airshipENS_14default_deleteIS3_EEED1B8ne200100Ev
+ __ZNSt3__111__call_onceERVmPvPFvS2_E
+ __ZNSt3__112shared_mutexD1B8ne200100Ev
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZN7support9transport7airshipC1ENS4_8protocolEE3$_1EEEEEvPv
+ __ZNSt3__119__shared_mutex_baseC1Ev
+ __ZNSt3__120__shared_ptr_emplaceINS_5mutexENS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceINS_5mutexENS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceINS_5mutexENS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceINS_5mutexENS_9allocatorIS1_EEED1Ev
+ __ZNSt3__122condition_variable_anyD1Ev
+ __ZNSt3__15alignEmmRPvRm
+ __ZNSt3__18functionIFvvEED2Ev
+ __ZNSt9bad_allocC1Ev
+ __ZNSt9bad_allocD0Ev
+ __ZNSt9bad_allocD1Ev
+ __ZTINSt3__110__function6__baseIFvvEEE
+ __ZTINSt3__110__function6__funcIZN7support9transport7airshipC1ENS4_8protocolEE3$_0NS_9allocatorIS6_EEFvvEEE
+ __ZTINSt3__120__shared_ptr_emplaceINS_5mutexENS_9allocatorIS1_EEEE
+ __ZTISt9bad_alloc
+ __ZTIZN7support9transport7airshipC1ENS1_8protocolEE3$_0
+ __ZTSNSt3__110__function6__baseIFvvEEE
+ __ZTSNSt3__110__function6__funcIZN7support9transport7airshipC1ENS4_8protocolEE3$_0NS_9allocatorIS6_EEFvvEEE
+ __ZTSNSt3__120__shared_ptr_emplaceINS_5mutexENS_9allocatorIS1_EEEE
+ __ZTSZN7support9transport7airshipC1ENS1_8protocolEE3$_0
+ __ZTVNSt3__110__function6__funcIZN7support9transport7airshipC1ENS4_8protocolEE3$_0NS_9allocatorIS6_EEFvvEEE
+ __ZTVNSt3__120__shared_ptr_emplaceINS_5mutexENS_9allocatorIS1_EEEE
+ __ZTVSt9bad_alloc
+ ___CFConstantStringClassReference
+ ___block_descriptor_tmp.111
+ ___block_descriptor_tmp.120
+ _aligned_alloc
+ _kIOMainPortDefault
- ___block_descriptor_tmp.109
- ___block_descriptor_tmp.119
CStrings:
+ "%s stopping..."
+ "/AppleInternal/Library/BuildRoots/4~B8cwugAGmdjprb_1eGONX2YOY1IF5UlRnfGuLqs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "airship"
+ "airship.io"
+ "already started"
+ "already stopped"
+ "com.apple.telephony.basebandservices.airship"
+ "error: airship not supported"
+ "error: failed to cast to internal type"
+ "error: failed to create dispatch group"
+ "error: failed to create io timer"
+ "error: failed to find io matching service for airship"
+ "error: failed to find property %@"
+ "error: failed to stop"
+ "error: invalid bytes read argument"
+ "error: invalid dest address"
+ "error: invalid dest size %zu (must be at least %zu)"
+ "error: invalid dispatch queue"
+ "error: invalid protocol"
+ "error: invalid source address"
+ "error: invalid state"
+ "error: io timeout, aborting..."
+ "error: read failed (timeout)"
+ "error: read size mismatch; expected: %u, actual: %u"
+ "error: write failed (timeout)"
+ "read scheduled for tid %zu, remaining %zu bytes..."
+ "read success (%zu bytes)"
+ "read success, remaining %zu bytes..."
+ "reading %u byte(s)"
+ "reading..."
+ "warning: memory pool dynamic allocation count increased by %zu for %s"
+ "write scheduled for tid %zu, remaining %zu bytes..."
+ "write success, remaining %zu bytes..."
+ "writing %u byte(s)"
- "/AppleInternal/Library/BuildRoots/4~B7lMugCYZKoXa_t5tjJP-HcYJp-av9SyMYxZyNM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"

```
