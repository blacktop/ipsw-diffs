## libswiftCore.dylib

> `/System/ExclaveKit/usr/lib/swift/libswiftCore.dylib`

```diff

-6.0.3.1.5
-  __TEXT.__text: 0x31b0cc
-  __TEXT.__auth_stubs: 0xa30
+6.0.3.1.6
+  __TEXT.__text: 0x31be78
+  __TEXT.__auth_stubs: 0xa40
   __TEXT.__objc_stubs: 0x140
   __TEXT.__init_offsets: 0x18
   __TEXT.__objc_methlist: 0xfb4
   __TEXT.__const: 0xb017b
-  __TEXT.__cstring: 0x1082e
+  __TEXT.__cstring: 0x10c68
   __TEXT.__objc_methname: 0x891
   __TEXT.__swift5_typeref: 0x5da7
   __TEXT.__swift5_capture: 0x2e8

   __TEXT.__objc_classname: 0x139
   __TEXT.__objc_methtype: 0x268
   __TEXT.__gcc_except_tab: 0xb8
-  __TEXT.__unwind_info: 0xaa98
+  __TEXT.__unwind_info: 0xaaa0
   __TEXT.__eh_frame: 0x9640
-  __DATA.__auth_got: 0x528
+  __DATA.__auth_got: 0x530
   __DATA.__got: 0x50
   __DATA.__auth_ptr: 0x50
   __DATA.__const: 0x135f0

   __DATA.__data: 0x104b0
   __DATA.__thread_vars: 0x18
   __DATA.__thread_bss: 0x10
-  __DATA.__common: 0x78
-  __DATA.__bss: 0xdb0
+  __DATA.__common: 0x88
+  __DATA.__bss: 0xe30
   - /System/ExclaveKit/usr/lib/libSystem.dylib
   - /System/ExclaveKit/usr/lib/libc++.dylib
   - /System/ExclaveKit/usr/lib/libobjc.A.dylib
-  Functions: 23721
-  Symbols:   41779
-  CStrings:  2765
+  Functions: 23731
+  Symbols:   41793
+  CStrings:  2778
 
Symbols:
+ _ZN22LibPrespecializedState23computeMapConfigurationEPKN5swift21LibPrespecializedDataINS0_9InProcessEEE.cold.1
+ _ZN22LibPrespecializedStateC2Ev.cold.1
+ _ZN22LibPrespecializedStateC2Ev.cold.2
+ _ZN22LibPrespecializedStateC2Ev.cold.3
+ _ZN5swift34getLibPrespecializedTypeDescriptorEPNS_8Demangle9__runtime4NodeE.cold.1
+ __ZL15SharedCacheInfo
+ __ZL36_searchTypeMetadataRecordsInSectionsIN5swift23ConcurrentReadableArrayIN12_GLOBAL__N_115ProtocolSectionEEEEPKNS0_23TargetContextDescriptorINS0_9InProcessEEERT_PNS0_8Demangle9__runtime4NodeE
+ __ZL36_searchTypeMetadataRecordsInSectionsIN5swift23ConcurrentReadableArrayIN12_GLOBAL__N_119TypeMetadataSectionEEEEPKNS0_23TargetContextDescriptorINS0_9InProcessEEERT_PNS0_8Demangle9__runtime4NodeE
+ __ZN24TypeMetadataPrivateStateC2Ev
+ __ZN5swift23ConcurrentReadableArrayIN12_GLOBAL__N_115ProtocolSectionEE9push_backERKS2_
+ __ZN5swift23ConcurrentReadableArrayIN12_GLOBAL__N_119TypeMetadataSectionEE9push_backERKS2_
+ __ZN5swift32ExpandResolvedSymbolicReferencesclENS_8Demangle9__runtime21SymbolicReferenceKindEPKv
+ __ZN5swift34getLibPrespecializedTypeDescriptorEPNS_8Demangle9__runtime4NodeE
+ __ZN5swift4LazyI20SharedCacheInfoStateE19defaultInitCallbackEPv
+ __ZN5swift7runtime11environment55SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_METADATA_variableE
+ __ZN5swift7runtime11environment64SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_DESCRIPTOR_LOOKUP_variableE
+ __ZN5swift7runtime11environment66SWIFT_DEBUG_VALIDATE_LIB_PRESPECIALIZED_DESCRIPTOR_LOOKUP_variableE
+ __ZN5swift7runtime11environment70SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_DESCRIPTOR_LOOKUP_isSet_variableE
+ __ZN5swift8Demangle9__runtime4Node12replaceChildEjPS2_
+ __ZNK5swift21PrebuiltStringMapBase4hashEPKvm
+ __ZNK5swift21PrebuiltStringMapBase9findIndexIZNKS_17PrebuiltStringMapIPKcPNS_14TargetMetadataINS_9InProcessEEEXadL_ZNS_21LibPrespecializedDataIS6_E12stringIsNullES4_EEE4findES4_mEUlmE_EENSt3__18optionalImEEPKvmRKT_
+ __dyld_is_preoptimized_objc_image_loaded
- _ZL21findLibPrespecializedv.cold.1
- _ZL29disablePrespecializedMetadata.0
- __ZL20disableForValidation
- __ZL21findLibPrespecializedv
- __ZN5swift7runtime11environment46SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_variableE
- __ZNK5swift17PrebuiltStringMapIPKcPNS_14TargetMetadataINS_9InProcessEEEXadL_ZNS_21LibPrespecializedDataIS4_E12stringIsNullES2_EEE4hashEPKvm
- __ZZZN5swift24getLibPrespecializedDataEvENK3$_0clEvE7TheLazy
- __ZZZN5swift24getLibPrespecializedDataEvENK3$_0clEvENUlPvE_8__invokeES1_
CStrings:
+ "Disabling metadata, SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_METADATA is false."
+ "Prespecializations library: %s\n"
+ "Prespecializations library: Descriptor table lookup of '%.*s' returned NULL pointer to descriptor pointer.\n"
+ "Prespecializations library: Did not find descriptor for key '%.*s'.\n"
+ "Prespecializations library: Failed to build demangling for node %p.\n"
+ "Prespecializations library: Failed to build demangling for simplified node %p.\n\n"
+ "Prespecializations library: Failed to build simplified mangling for node %p.\n"
+ "Prespecializations library: Found descriptor %p for key '%.*s'.\n"
+ "Prespecializations library: Hash table lookup checked %u loaded entries, %u total entries, starting data pointer %p, starting auxiliary pointer %p.\n"
+ "Prespecializations library: Looking up descriptor named '%.*s'.\n"
+ "Prespecializations library: Returning data pointer %p\n"
+ "Prespecializations library: Setting descriptorMapEnabled=%s from SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_DESCRIPTOR_LOOKUP.\n"
+ "Prespecializations library: Setting descriptorMapEnabled=%s from the option flags.\n"
+ "Searching for type descriptor, prespecialized descriptor map returned %p, but scan returned %p. Node tree:\n%s"
- "Prespecializations library: Disabling, SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED = %d\n"

```
