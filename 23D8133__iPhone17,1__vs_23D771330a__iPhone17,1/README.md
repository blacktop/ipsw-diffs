# 23D8133 .vs 23D771330a

## OTAs

- `23D8133__iPhone17,1`
- `23D771330a__iPhone17,1`

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| Patched OTA *(23D8133)* | 623.2.7.10.4 |
| Patched OTA *(23D771330a)* | 623.2.7.110.1 |

### Dylibs

#### ⬆️ Updated (6)

<details>
  <summary><i>View Updated</i></summary>

#### ProductKit

>  `/System/Library/PrivateFrameworks/ProductKit.framework/ProductKit`

```diff

-129.400.11.2.4
-  __TEXT.__text: 0x64154
+129.400.11.2.2
+  __TEXT.__text: 0x63f94
   __TEXT.__auth_stubs: 0x1e80
   __TEXT.__objc_methlist: 0x618
-  __TEXT.__const: 0x5fcc
+  __TEXT.__const: 0x5fac
   __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__cstring: 0x2964
+  __TEXT.__cstring: 0x2914
   __TEXT.__oslogstring: 0x1bd3
   __TEXT.__swift5_typeref: 0x1810
-  __TEXT.__swift5_reflstr: 0x1ce3
+  __TEXT.__swift5_reflstr: 0x1ca3
   __TEXT.__swift5_assocty: 0x710
   __TEXT.__constg_swiftt: 0x1878
-  __TEXT.__swift5_fieldmd: 0x2558
+  __TEXT.__swift5_fieldmd: 0x24f8
   __TEXT.__swift5_builtin: 0x140
   __TEXT.__swift5_proto: 0x3a0
   __TEXT.__swift5_types: 0x1d4

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x18
   __AUTH_CONST.__auth_got: 0xf50
-  __AUTH_CONST.__const: 0x4c28
+  __AUTH_CONST.__const: 0x4c18
   __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__objc_const: 0x1458
   __AUTH.__objc_data: 0x800

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 16F203DB-1540-37D3-A425-AD4DB581E414
+  UUID: FF372DCB-64D0-369B-9F1B-38D3E4CC5B21
   Functions: 2178
   Symbols:   1483
-  CStrings:  1040
+  CStrings:  1032
 
Functions:
~ sub_2657d4504 : 6744 -> 6520
~ sub_2657d5f5c -> sub_2657d5e7c : 204 -> 172
~ sub_2657d6088 -> sub_2657d5f88 : 6644 -> 6484
~ sub_2657d7a7c -> sub_2657d78dc : 1228 -> 1196
CStrings:
- "Mac17,6"
- "Mac17,7"
- "Mac17,8"
- "Mac17,9"
- "iPad16,10"
- "iPad16,11"
- "iPad16,8"
- "iPad16,9"

```

#### ProductKitCore

>  `/System/Library/PrivateFrameworks/ProductKitCore.framework/ProductKitCore`

```diff

-129.400.11.2.4
-  __TEXT.__text: 0x4e7b8
+129.400.11.2.2
+  __TEXT.__text: 0x4e604
   __TEXT.__auth_stubs: 0x1590
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0x5234
-  __TEXT.__cstring: 0x1dbe
+  __TEXT.__const: 0x5194
+  __TEXT.__cstring: 0x1d6e
   __TEXT.__constg_swiftt: 0xdbc
   __TEXT.__swift5_typeref: 0xe78
-  __TEXT.__swift5_reflstr: 0x17ca
-  __TEXT.__swift5_fieldmd: 0x1c9c
+  __TEXT.__swift5_reflstr: 0x178a
+  __TEXT.__swift5_fieldmd: 0x1c3c
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_assocty: 0x368
   __TEXT.__oslogstring: 0x1791

   __DATA_CONST.__objc_selrefs: 0x258
   __DATA_CONST.__objc_protorefs: 0x10
   __AUTH_CONST.__auth_got: 0xac8
-  __AUTH_CONST.__const: 0x2d80
+  __AUTH_CONST.__const: 0x2d70
   __AUTH_CONST.__objc_const: 0x798
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x9f8

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E91675E9-ADF0-36E3-B8FB-65160F98D505
+  UUID: 4C08F48B-F9C0-3C3D-896C-91B89D2F7A54
   Functions: 1551
   Symbols:   738
-  CStrings:  647
+  CStrings:  639
 
Functions:
~ sub_2a34c39fc : 6728 -> 6504
~ sub_2a34c5444 -> sub_2a34c5364 : 204 -> 172
~ sub_2a34c5510 -> sub_2a34c5410 : 6644 -> 6496
~ sub_2a34c6f04 -> sub_2a34c6d70 : 1228 -> 1196
CStrings:
- "Mac17,6"
- "Mac17,7"
- "Mac17,8"
- "Mac17,9"
- "iPad16,10"
- "iPad16,11"
- "iPad16,8"
- "iPad16,9"

```

#### SettingsFoundation

>  `/System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation`

```diff

-1087.3.2.100.0
-  __TEXT.__text: 0x126ec
+1087.3.2.0.0
+  __TEXT.__text: 0x12244
   __TEXT.__auth_stubs: 0x7e0
   __TEXT.__objc_methlist: 0x67c
-  __TEXT.__const: 0x9c0
-  __TEXT.__cstring: 0x1b78
+  __TEXT.__const: 0x800
+  __TEXT.__cstring: 0x1b63
   __TEXT.__ustring: 0x78
   __TEXT.__oslogstring: 0x182c
   __TEXT.__gcc_except_tab: 0x28

   __DATA_CONST.__objc_arraydata: 0xb0
   __AUTH_CONST.__auth_got: 0x400
   __AUTH_CONST.__const: 0x480
-  __AUTH_CONST.__cfstring: 0x23a0
+  __AUTH_CONST.__cfstring: 0x2380
   __AUTH_CONST.__objc_const: 0x950
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0x48

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 75D665D9-4CD5-3FE6-96B0-3C343C9999CB
-  Functions: 346
-  Symbols:   1322
-  CStrings:  1081
+  UUID: 1E19CE59-2F2D-3395-8A27-BE5286C21090
+  Functions: 345
+  Symbols:   1321
+  CStrings:  1079
 
Symbols:
+ _SFBuiltInRegulatoryImageForModelAndVariant.styleSensitiveImage.324
+ _SFBuiltInRegulatoryImageForModelAndVariant.styleSensitiveImage.331
+ ___block_literal_global.273
+ ___block_literal_global.275
+ ___block_literal_global.280
+ ___block_literal_global.282
+ ___block_literal_global.288
+ ___block_literal_global.369
+ ___block_literal_global.385
+ ___block_literal_global.390
+ ___block_literal_global.404
+ ___block_literal_global.412
+ ___block_literal_global.538
- _SFBuiltInRegulatoryImageForModelAndVariant.styleSensitiveImage.354
- _SFBuiltInRegulatoryImageForModelAndVariant.styleSensitiveImage.361
- _SFDeviceSupportsRFExposure2026OrLater
- ___block_literal_global.303
- ___block_literal_global.305
- ___block_literal_global.310
- ___block_literal_global.312
- ___block_literal_global.318
- ___block_literal_global.399
- ___block_literal_global.415
- ___block_literal_global.420
- ___block_literal_global.434
- ___block_literal_global.442
- ___block_literal_global.571
Functions:
- _SFDeviceSupportsRFExposure2026OrLater
~ _SFRFExposureDocumentHTMLString : 916 -> 892
CStrings:
- "RF_INTRO_IPHONE_2026"

```

#### libANGLE-shared.dylib

>  `/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libANGLE-shared.dylib`

```diff

-623.2.7.10.4
-  __TEXT.__text: 0x25bbe0
+623.2.7.110.1
+  __TEXT.__text: 0x25bc84
   __TEXT.__auth_stubs: 0xde0
-  __TEXT.__const: 0x82c40
-  __TEXT.__cstring: 0x41b17
+  __TEXT.__const: 0x82ca0
+  __TEXT.__cstring: 0x41bbc
   __TEXT.__gcc_except_tab: 0x295c
   __TEXT.__oslogstring: 0xf
   __TEXT.__unwind_info: 0x16a0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 997A2B9C-07E0-3E10-882F-2E9D527D3A80
+  UUID: 1FE72507-F91C-3AB9-9615-9FF61BC8758C
   Functions: 8929
   Symbols:   25259
-  CStrings:  7172
+  CStrings:  7175
 
Symbols:
+ __ZN2rx21ProvokingVertexHelper19generateIndexBufferEPNS_10ContextMtlEiiN2gl13PrimitiveModeENS3_16DrawElementsTypeERjRmRS4_RNSt3__110shared_ptrINS_3mtl6BufferEEE
+ __ZN2rx21ProvokingVertexHelper23preconditionIndexBufferEPNS_10ContextMtlENSt3__110shared_ptrINS_3mtl6BufferEEEimbN2gl13PrimitiveModeENS8_16DrawElementsTypeERjRmRS9_RS7_
- __ZN2rx21ProvokingVertexHelper19generateIndexBufferEPNS_10ContextMtlEmmN2gl13PrimitiveModeENS3_16DrawElementsTypeERmS6_RS4_RNSt3__110shared_ptrINS_3mtl6BufferEEE
- __ZN2rx21ProvokingVertexHelper23preconditionIndexBufferEPNS_10ContextMtlENSt3__110shared_ptrINS_3mtl6BufferEEEmmbN2gl13PrimitiveModeENS8_16DrawElementsTypeERmSB_RS9_RS7_
Functions:
~ __ZN2rx10ContextMtl14drawArraysImplEPKN2gl7ContextENS1_13PrimitiveModeEiiij : 2472 -> 2456
~ __ZN2rx10ContextMtl16drawElementsImplEPKN2gl7ContextENS1_13PrimitiveModeEiNS1_16DrawElementsTypeEPKviij : 1992 -> 1988
~ __ZN2rx21ProvokingVertexHelper23preconditionIndexBufferEPNS_10ContextMtlENSt3__110shared_ptrINS_3mtl6BufferEEEmmbN2gl13PrimitiveModeENS8_16DrawElementsTypeERmSB_RS9_RS7_ -> __ZN2rx21ProvokingVertexHelper23preconditionIndexBufferEPNS_10ContextMtlENSt3__110shared_ptrINS_3mtl6BufferEEEimbN2gl13PrimitiveModeENS8_16DrawElementsTypeERjRmRS9_RS7_ : 740 -> 832
~ __ZN2rx21ProvokingVertexHelper19generateIndexBufferEPNS_10ContextMtlEmmN2gl13PrimitiveModeENS3_16DrawElementsTypeERmS6_RS4_RNSt3__110shared_ptrINS_3mtl6BufferEEE -> __ZN2rx21ProvokingVertexHelper19generateIndexBufferEPNS_10ContextMtlEiiN2gl13PrimitiveModeENS3_16DrawElementsTypeERjRmRS4_RNSt3__110shared_ptrINS_3mtl6BufferEEE : 724 -> 816
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/ANGLE/Source/ThirdParty/ANGLE/src/libANGLE/renderer/metal/ProvokingVertexHelper.mm"
+ "generateIndexBuffer"
+ "preconditionIndexBuffer"

```

#### WebCore

>  `/System/Library/PrivateFrameworks/WebCore.framework/WebCore`

```diff

-623.2.7.10.4
-  __TEXT.__text: 0x325ebe4
+623.2.7.110.1
+  __TEXT.__text: 0x325ef34
   __TEXT.__auth_stubs: 0xd910
   __TEXT.__objc_methlist: 0x562c
   __TEXT.__getClass_cstr: 0x1151

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 9508ADC1-3E60-371B-8560-C3A6EEDF1B07
-  Functions: 126576
-  Symbols:   288168
+  UUID: 115B9731-6D8B-36A6-A502-565BD0E8C6F1
+  Functions: 126570
+  Symbols:   288154
   CStrings:  36963
 
Symbols:
+ __ZN3WTF6VectorINS_17CompletionHandlerIFvvEEELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEEaSEOS6_
+ __ZN3WTF9HashTableINS_23ObjectIdentifierGenericIN7WebCore39ServiceWorkerRegistrationIdentifierTypeENS_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEENS_12KeyValuePairIS6_NS_3RefINS2_20SWServerRegistrationENS_12RawPtrTraitsIS9_EENS_21DefaultRefDerefTraitsIS9_EEEEEENS_24KeyValuePairKeyExtractorISF_EENS_11DefaultHashIS6_EENS_7HashMapIS6_SE_SJ_NS_10HashTraitsIS6_EENSL_ISE_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE1ENS_10FastMallocEE18KeyValuePairTraitsESM_SQ_E6lookupINS_24HashMapTranslatorAdapterISS_NS_22IdentityHashTranslatorISS_SJ_EEEELSP_1ES6_EEPSF_RKT1_
+ __ZNK3WTF10RefCountedIN7WebCore20SWServerRegistrationEE5derefEv
- __ZN3WTF17GenericHashTraitsINS_12KeyValuePairINS_6StringEN7WebCore16ProcessQualifiedINS_4UUIDEEEEEE13assignToEmptyIS7_S7_EEvRT_OT0_
- __ZN3WTF22IdentityHashTranslatorINS_7HashMapIN7WebCore16ProcessQualifiedINS_4UUIDEEENS_7WeakRefINS2_20SWServerRegistrationENS_18DefaultWeakPtrImplEEENS_11DefaultHashIS5_EENS_10HashTraitsIS5_EENSC_IS9_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE1ENS_10FastMallocEE18KeyValuePairTraitsESB_E4hashIS5_EEjRKT_
- __ZN3WTF7HashMapIN7WebCore12ClientOriginENS1_8SWServer7ClientsENS_11DefaultHashIS2_EENS_10HashTraitsIS2_EENS7_IS4_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE1ENS_10FastMallocEE4findERKS2_
- __ZN3WTF7HashMapIN7WebCore16ProcessQualifiedINS_4UUIDEEENS_23ObjectIdentifierGenericINS1_39ServiceWorkerRegistrationIdentifierTypeENS_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEENS_11DefaultHashIS4_EENS_10HashTraitsIS4_EENSC_IS9_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE1ENS_10FastMallocEE4findERKS4_
- __ZN3WTF7HashMapIN7WebCore16ProcessQualifiedINS_4UUIDEEENS_23ObjectIdentifierGenericINS1_39ServiceWorkerRegistrationIdentifierTypeENS_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEENS_11DefaultHashIS4_EENS_10HashTraitsIS4_EENSC_IS9_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE1ENS_10FastMallocEE6removeENS_24HashTableIteratorAdapterINS_9HashTableIS4_NS_12KeyValuePairIS4_S9_EENS_24KeyValuePairKeyExtractorISM_EESB_NSI_18KeyValuePairTraitsESD_SH_EESM_EE
- __ZN3WTF9HashTableIN7WebCore16ProcessQualifiedINS_4UUIDEEENS_12KeyValuePairIS4_NS_9UniqueRefINS1_23ServiceWorkerClientDataEEEEENS_24KeyValuePairKeyExtractorIS9_EENS_11DefaultHashIS4_EENS_7HashMapIS4_S8_SD_NS_10HashTraitsIS4_EENSF_IS8_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE1ENS_10FastMallocEE18KeyValuePairTraitsESG_SK_E6shrinkEv
- __ZN7WebCore16SWServerJobQueue27cancelJobsFromServiceWorkerEN3WTF23ObjectIdentifierGenericINS_27ServiceWorkerIdentifierTypeENS1_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEE
- __ZNK3WTF10RefCountedIN7WebCore14SWServerWorkerEE5derefEv
- __ZNK3WTF27RefCountedAndCanMakeWeakPtrIN7WebCore20SWServerRegistrationEE5derefEv
- __ZNK3WTF7HashMapINS_23ObjectIdentifierGenericIN7WebCore39ServiceWorkerRegistrationIdentifierTypeENS_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEENS_3RefINS2_20SWServerRegistrationENS_12RawPtrTraitsIS8_EENS_21DefaultRefDerefTraitsIS8_EEEENS_11DefaultHashIS6_EENS_10HashTraitsIS6_EENSG_ISD_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE1ENS_10FastMallocEE3getERKS6_
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ARM64Assembler.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/AbstractSlotVisitorInlines.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArgList.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArrayBuffer.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArrayBufferView.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DataView.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DisallowVMEntry.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ExecutableAllocator.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/GenericTypedArrayViewInlines.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/IndexingHeader.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArray.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArrayBufferViewInlines.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSCPtrTag.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSCast.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSObject.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSObjectInlines.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/MacroAssemblerARM64.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/SecureARM64EHashPinsInlines.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/WebKitAdditions/EventHandlerIOSTouch.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/Box.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/CheckedArithmetic.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/CheckedPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/CompactVariantOperations.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/CryptographicUtilities.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/Deque.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/HashTable.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/IndexedRange.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/JSONValues.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/Markable.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/Ref.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/RefCounted.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/RefPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/RetainPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/WeakPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/WeakRef.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/cocoa/TypeCastsCocoa.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
+ "void JSC::SecureARM64EHashPins::forEachPage(Function) [Function = (lambda at /AppleInternal/Library/BuildRoots/4~CKOXugAg7XpVzRwaJei0IVfosw0IdC6fiSSvHlo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/SecureARM64EHashPinsInlines.h:65:17)]"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ARM64Assembler.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/AbstractSlotVisitorInlines.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArgList.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArrayBuffer.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArrayBufferView.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DataView.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DisallowVMEntry.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ExecutableAllocator.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/GenericTypedArrayViewInlines.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/IndexingHeader.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArray.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArrayBufferViewInlines.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSCPtrTag.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSCast.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSObject.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSObjectInlines.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/MacroAssemblerARM64.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/SecureARM64EHashPinsInlines.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/WebKitAdditions/EventHandlerIOSTouch.cpp"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/Box.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/CheckedArithmetic.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/CheckedPtr.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/CompactVariantOperations.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/CryptographicUtilities.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/Deque.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/HashTable.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/IndexedRange.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/JSONValues.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/Markable.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/Ref.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/RefCounted.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/RefPtr.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/RetainPtr.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/WeakPtr.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/WeakRef.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/cocoa/TypeCastsCocoa.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
- "/AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
- "void JSC::SecureARM64EHashPins::forEachPage(Function) [Function = (lambda at /AppleInternal/Library/BuildRoots/4~CILLugCSAvBxDRKw7GhsVpPKAwYznrvjmlE1L5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/SecureARM64EHashPinsInlines.h:65:17)]"

```

#### WebGPU

>  `/System/Library/PrivateFrameworks/WebGPU.framework/WebGPU`

```diff

-623.2.7.10.4
-  __TEXT.__text: 0x245d14
+623.2.7.110.1
+  __TEXT.__text: 0x245e34
   __TEXT.__auth_stubs: 0x1450
   __TEXT.__objc_methlist: 0x9e0
   __TEXT.__const: 0x1bf4

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6B9187D9-71B7-3C99-AEA8-A03473298DB3
+  UUID: 948512B9-72A4-3548-BE1C-DA9ECFCA00AA
   Functions: 3488
-  Symbols:   7776
+  Symbols:   7778
   CStrings:  3801
 
Symbols:
+ __ZN3WTF6VectorINSt3__14pairIPN4WGSL3AST8FunctionENS_6StringEEELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEE14expandCapacityILNS_13FailureActionE0EEEPS8_mSE_
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CKOWugC7F2nan8MTGdiMvFm8nOGM50RmQEY8Ws0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOWugC7F2nan8MTGdiMvFm8nOGM50RmQEY8Ws0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/HashTable.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOWugC7F2nan8MTGdiMvFm8nOGM50RmQEY8Ws0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/Markable.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOWugC7F2nan8MTGdiMvFm8nOGM50RmQEY8Ws0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/RefCounted.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOWugC7F2nan8MTGdiMvFm8nOGM50RmQEY8Ws0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOWugC7F2nan8MTGdiMvFm8nOGM50RmQEY8Ws0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOWugC7F2nan8MTGdiMvFm8nOGM50RmQEY8Ws0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/WeakPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOWugC7F2nan8MTGdiMvFm8nOGM50RmQEY8Ws0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
+ "/AppleInternal/Library/BuildRoots/4~CKOWugC7F2nan8MTGdiMvFm8nOGM50RmQEY8Ws0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
- "/AppleInternal/Library/BuildRoots/4~CILJugAFaCqknM6LgSq6rLJPyT0qyFFg97xBkTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
- "/AppleInternal/Library/BuildRoots/4~CILJugAFaCqknM6LgSq6rLJPyT0qyFFg97xBkTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/HashTable.h"
- "/AppleInternal/Library/BuildRoots/4~CILJugAFaCqknM6LgSq6rLJPyT0qyFFg97xBkTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/Markable.h"
- "/AppleInternal/Library/BuildRoots/4~CILJugAFaCqknM6LgSq6rLJPyT0qyFFg97xBkTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/RefCounted.h"
- "/AppleInternal/Library/BuildRoots/4~CILJugAFaCqknM6LgSq6rLJPyT0qyFFg97xBkTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/4~CILJugAFaCqknM6LgSq6rLJPyT0qyFFg97xBkTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
- "/AppleInternal/Library/BuildRoots/4~CILJugAFaCqknM6LgSq6rLJPyT0qyFFg97xBkTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/WeakPtr.h"
- "/AppleInternal/Library/BuildRoots/4~CILJugAFaCqknM6LgSq6rLJPyT0qyFFg97xBkTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
- "/AppleInternal/Library/BuildRoots/4~CILJugAFaCqknM6LgSq6rLJPyT0qyFFg97xBkTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"

```


</details>

## Files

### 🆕 New

#### SystemOS (8)

- `.fseventsd/ffba01048d75cae2`
- `.fseventsd/ffba01048d75cae3`
- `.fseventsd/ffba01048d9a1ca5`
- `.fseventsd/ffba01048d9a1ca6`
- `.fseventsd/ffba01048da4ee6c`
- `.fseventsd/ffba01048da4ee6d`
- `.fseventsd/ffba01048da55d87`
- `.fseventsd/ffba01048da55d88`

#### AppOS (8)

- `.fseventsd/ffba01048d75ca85`
- `.fseventsd/ffba01048d75ca86`
- `.fseventsd/ffba01048d9a1c62`
- `.fseventsd/ffba01048d9a1c63`
- `.fseventsd/ffba01048da4ee00`
- `.fseventsd/ffba01048da4ee01`
- `.fseventsd/ffba01048da55d35`
- `.fseventsd/ffba01048da55d36`

### ❌ Removed

#### SystemOS (10)

- `.fseventsd/ffba01048d75ca4e`
- `.fseventsd/ffba01048d75ca4f`
- `.fseventsd/ffba01048d9a1c43`
- `.fseventsd/ffba01048d9a1c44`
- `.fseventsd/ffba01048da4ede7`
- `.fseventsd/ffba01048da4ede8`
- `.fseventsd/ffba01048da4ede9`
- `.fseventsd/ffba01048da4edea`
- `.fseventsd/ffba01048da55cfe`
- `.fseventsd/ffba01048da55cff`

#### AppOS (8)

- `.fseventsd/ffba01048d75c992`
- `.fseventsd/ffba01048d75c993`
- `.fseventsd/ffba01048d9a1bfe`
- `.fseventsd/ffba01048d9a1bff`
- `.fseventsd/ffba01048da4edc2`
- `.fseventsd/ffba01048da4edc3`
- `.fseventsd/ffba01048da55b00`
- `.fseventsd/ffba01048da55b01`

## EOF
