## Intents

> `/System/Library/Frameworks/Intents.framework/Intents`

```diff

-4015.2.3.0.0
-  __TEXT.__text: 0x4519dc
-  __TEXT.__auth_stubs: 0xfd0
-  __TEXT.__objc_methlist: 0x78c04
+4015.3.3.0.0
+  __TEXT.__text: 0x452738
+  __TEXT.__auth_stubs: 0x1000
+  __TEXT.__objc_methlist: 0x78c3c
   __TEXT.__const: 0x1eb0
   __TEXT.__dlopen_cstrs: 0xce9
-  __TEXT.__gcc_except_tab: 0x23f0
-  __TEXT.__oslogstring: 0x587b
-  __TEXT.__cstring: 0x47676
+  __TEXT.__gcc_except_tab: 0x242c
+  __TEXT.__oslogstring: 0x59da
+  __TEXT.__cstring: 0x47799
   __TEXT.__ustring: 0x512
-  __TEXT.__unwind_info: 0x10e50
+  __TEXT.__unwind_info: 0x10e68
   __TEXT.__objc_classname: 0x12221
-  __TEXT.__objc_methname: 0x69eaa
-  __TEXT.__objc_methtype: 0xcc6a
-  __TEXT.__objc_stubs: 0x33c00
+  __TEXT.__objc_methname: 0x69f90
+  __TEXT.__objc_methtype: 0xcc8d
+  __TEXT.__objc_stubs: 0x33ca0
   __DATA_CONST.__got: 0x2898
   __DATA_CONST.__const: 0xb8d0
   __DATA_CONST.__objc_classlist: 0x2930
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x1940
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15440
+  __DATA_CONST.__objc_selrefs: 0x15470
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x1398
   __DATA_CONST.__objc_arraydata: 0xc7f8
-  __AUTH_CONST.__auth_got: 0x800
+  __AUTH_CONST.__auth_got: 0x818
   __AUTH_CONST.__const: 0x1780
-  __AUTH_CONST.__cfstring: 0x428e0
-  __AUTH_CONST.__objc_const: 0xb4d28
+  __AUTH_CONST.__cfstring: 0x429a0
+  __AUTH_CONST.__objc_const: 0xb4d58
   __AUTH_CONST.__objc_intobj: 0x828
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x4da0
   __AUTH_CONST.__objc_dictobj: 0x3b60
   __AUTH.__objc_data: 0x144b0
-  __DATA.__objc_ivar: 0x3d4c
+  __DATA.__objc_ivar: 0x3d50
   __DATA.__data: 0x12f98
   __DATA.__bss: 0xc60
   __DATA.__common: 0x8

   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8D2F84BD-79F6-328D-AC72-B8EF6F9195A2
-  Functions: 30627
-  Symbols:   87236
-  CStrings:  37228
+  UUID: E751FAB9-7F01-3BAB-B328-DCF5A686383B
+  Functions: 30632
+  Symbols:   87255
+  CStrings:  37257
 
Symbols:
+ +[INHelperServiceAccessSpecifier accessSpecifierFilteredForAssociatedAppBundleIdentifier:auditToken:]
+ -[INHelperServiceAccessSpecifier associatedAuditToken]
+ -[INHelperServiceAccessSpecifier initWithAccessLevel:associatedAppBundleIdentifier:auditToken:]
+ -[INImageFilePersistence _validateImageData:error:]
+ -[INImageServiceConnection _validateImageData:error:]
+ -[_INURLImage(INPortableImageLoader) _validateFileURLAccess:accessSpecifier:error:]
+ -[_INURLImage(INPortableImageLoader) _validateFileURLAccess:error:]
+ GCC_except_table13195
+ GCC_except_table13727
+ GCC_except_table13766
+ GCC_except_table13770
+ GCC_except_table14015
+ GCC_except_table14542
+ GCC_except_table15220
+ GCC_except_table15224
+ GCC_except_table16363
+ GCC_except_table16466
+ GCC_except_table16474
+ GCC_except_table16475
+ GCC_except_table16777
+ GCC_except_table18423
+ GCC_except_table19079
+ GCC_except_table19249
+ GCC_except_table19276
+ GCC_except_table19841
+ GCC_except_table19843
+ GCC_except_table19846
+ GCC_except_table19924
+ GCC_except_table20924
+ GCC_except_table21019
+ GCC_except_table21241
+ GCC_except_table22309
+ GCC_except_table22312
+ GCC_except_table22315
+ GCC_except_table22930
+ GCC_except_table22947
+ GCC_except_table23663
+ GCC_except_table25137
+ GCC_except_table25149
+ GCC_except_table27023
+ GCC_except_table27024
+ GCC_except_table27025
+ GCC_except_table27026
+ GCC_except_table28723
+ GCC_except_table28725
+ GCC_except_table28733
+ GCC_except_table28735
+ GCC_except_table28744
+ GCC_except_table29792
+ GCC_except_table29806
+ GCC_except_table29807
+ GCC_except_table29816
+ GCC_except_table29817
+ GCC_except_table29818
+ GCC_except_table29820
+ GCC_except_table30009
+ _CGImageSourceCopyPropertiesAtIndex
+ _CGImageSourceCreateWithData
+ _ChronoServicesLibraryCore.frameworkLibrary.123736
+ _ContactsLibraryCore.frameworkLibrary.111157
+ _CoreGraphicsLibrary.136773
+ _CoreGraphicsLibraryCore.frameworkLibrary.136778
+ _CoreSpotlightLibraryCore.frameworkLibrary.79800
+ _HealthKitLibraryCore.frameworkLibrary.95524
+ _IntentsUILibraryCore.frameworkLibrary.83673
+ _LinkServicesLibraryCore.frameworkLibrary.166081
+ _OBJC_IVAR_$_INHelperServiceAccessSpecifier._associatedAuditToken
+ _VoiceShortcutClientLibraryCore.frameworkLibrary.113100
+ _VoiceShortcutClientLibraryCore.frameworkLibrary.123659
+ ___32-[INImageServiceConnection init]_block_invoke.13
+ ___77-[INImageServiceConnection fetchShareExtensionIntentForExtensionContextUUID:]_block_invoke.79
+ ___79-[INImageServiceConnection storeImage:scaled:qualityOfService:storeType:error:]_block_invoke.84
+ ___97-[_INURLImage(INPortableImageLoader) _loadImageDataAndSizeWithHelper:accessSpecifier:completion:]_block_invoke.130
+ ___97-[_INURLImage(INPortableImageLoader) _loadImageDataAndSizeWithHelper:accessSpecifier:completion:]_block_invoke.132
+ ___97-[_INURLImage(INPortableImageLoader) _loadImageDataAndSizeWithHelper:accessSpecifier:completion:]_block_invoke.136
+ ___Block_byref_object_copy_.100578
+ ___Block_byref_object_copy_.104544
+ ___Block_byref_object_copy_.68266
+ ___Block_byref_object_copy_.69086
+ ___Block_byref_object_copy_.71947
+ ___Block_byref_object_copy_.75162
+ ___Block_byref_object_copy_.90493
+ ___Block_byref_object_dispose_.100579
+ ___Block_byref_object_dispose_.104545
+ ___Block_byref_object_dispose_.68267
+ ___Block_byref_object_dispose_.69087
+ ___Block_byref_object_dispose_.71948
+ ___Block_byref_object_dispose_.75163
+ ___Block_byref_object_dispose_.90494
+ ___ChronoServicesLibraryCore_block_invoke.123737
+ ___ContactsLibraryCore_block_invoke.111158
+ ___CoreGraphicsLibraryCore_block_invoke.136779
+ ___CoreSpotlightLibraryCore_block_invoke.79801
+ ___HealthKitLibraryCore_block_invoke.95525
+ ___IntentsUILibraryCore_block_invoke.83674
+ ___LinkServicesLibraryCore_block_invoke.166082
+ ___VoiceShortcutClientLibraryCore_block_invoke.113101
+ ___VoiceShortcutClientLibraryCore_block_invoke.123660
+ ___block_literal_global.10.103510
+ ___block_literal_global.100324
+ ___block_literal_global.100499
+ ___block_literal_global.103500
+ ___block_literal_global.104645
+ ___block_literal_global.105661
+ ___block_literal_global.11.111801
+ ___block_literal_global.111829
+ ___block_literal_global.119943
+ ___block_literal_global.12.158359
+ ___block_literal_global.123759
+ ___block_literal_global.13.103512
+ ___block_literal_global.13.98812
+ ___block_literal_global.158347
+ ___block_literal_global.3.111800
+ ___block_literal_global.5.94179
+ ___block_literal_global.6.111812
+ ___block_literal_global.6.72063
+ ___block_literal_global.68352
+ ___block_literal_global.68469
+ ___block_literal_global.69088
+ ___block_literal_global.70491
+ ___block_literal_global.71
+ ___block_literal_global.71253
+ ___block_literal_global.71997
+ ___block_literal_global.72059
+ ___block_literal_global.75020
+ ___block_literal_global.76.75073
+ ___block_literal_global.77387
+ ___block_literal_global.82396
+ ___block_literal_global.87
+ ___block_literal_global.91.71998
+ ___block_literal_global.91461
+ ___block_literal_global.92319
+ ___block_literal_global.94203
+ ___block_literal_global.98823
+ ___getCGColorCreateSRGBSymbolLoc_block_invoke.136824
+ ___getCGColorGetComponentsSymbolLoc_block_invoke.136772
+ ___getCNPostalAddressClass_block_invoke.111156
+ ___getCSSearchableItemAttributeSetClass_block_invoke.79799
+ ___getHKUnitClass_block_invoke.95523
+ _audit_stringChronoServices.123742
+ _audit_stringContacts.111163
+ _audit_stringCoreGraphics.136781
+ _audit_stringCoreSpotlight.79806
+ _audit_stringHealthKit.95530
+ _audit_stringLinkServices.166087
+ _audit_stringVoiceShortcutClient.113106
+ _audit_stringVoiceShortcutClient.123665
+ _getCGColorCreateSRGBSymbolLoc.ptr.136823
+ _getCGColorGetComponentsSymbolLoc.ptr.136771
+ _getCNPostalAddressClass.softClass.111155
+ _getCSSearchableItemAttributeSetClass.softClass.79798
+ _getHKUnitClass.95521
+ _getHKUnitClass.softClass.95522
+ _intentDescription.intentDescription.68470
+ _intentDescription.onceToken.68468
+ _objc_msgSend$_validateFileURLAccess:accessSpecifier:error:
+ _objc_msgSend$_validateImageData:error:
+ _objc_msgSend$accessSpecifierFilteredForAssociatedAppBundleIdentifier:auditToken:
+ _objc_msgSend$associatedAuditToken
+ _objc_msgSend$dataWithContentsOfURL:
+ _objc_msgSend$initWithAccessLevel:associatedAppBundleIdentifier:auditToken:
+ _objc_msgSend$initWithBytes:length:
+ _sandbox_check_by_audit_token
+ _serviceIdentifier.onceToken.83647
+ _serviceIdentifier.sServiceIdentifier.83648
+ _sharedCache.onceToken.82395
+ _sharedManager.onceToken.123758
+ _sharedManager.sharedManager.123760
+ _sharedProvider.onceToken.158358
- +[INHelperServiceAccessSpecifier accessSpecifierFilteredForAssociatedAppBundleIdentifier:]
- -[INHelperServiceAccessSpecifier initWithAccessLevel:associatedAppBundleIdentifier:]
- GCC_except_table13194
- GCC_except_table13726
- GCC_except_table13765
- GCC_except_table13769
- GCC_except_table14014
- GCC_except_table14541
- GCC_except_table15219
- GCC_except_table15223
- GCC_except_table16360
- GCC_except_table16463
- GCC_except_table16471
- GCC_except_table16472
- GCC_except_table16774
- GCC_except_table18420
- GCC_except_table19075
- GCC_except_table19245
- GCC_except_table19272
- GCC_except_table19837
- GCC_except_table19839
- GCC_except_table19842
- GCC_except_table19920
- GCC_except_table20920
- GCC_except_table21015
- GCC_except_table21236
- GCC_except_table22304
- GCC_except_table22307
- GCC_except_table22310
- GCC_except_table22925
- GCC_except_table22942
- GCC_except_table23658
- GCC_except_table25132
- GCC_except_table25144
- GCC_except_table27015
- GCC_except_table27018
- GCC_except_table27019
- GCC_except_table27021
- GCC_except_table28713
- GCC_except_table28720
- GCC_except_table28728
- GCC_except_table28730
- GCC_except_table28739
- GCC_except_table29787
- GCC_except_table29795
- GCC_except_table29796
- GCC_except_table29802
- GCC_except_table29803
- GCC_except_table29811
- GCC_except_table29812
- GCC_except_table30004
- _ChronoServicesLibraryCore.frameworkLibrary.123689
- _ContactsLibraryCore.frameworkLibrary.111118
- _CoreGraphicsLibrary.136726
- _CoreGraphicsLibraryCore.frameworkLibrary.136731
- _CoreSpotlightLibraryCore.frameworkLibrary.79784
- _HealthKitLibraryCore.frameworkLibrary.95495
- _IntentsUILibraryCore.frameworkLibrary.83657
- _LinkServicesLibraryCore.frameworkLibrary.166034
- _VoiceShortcutClientLibraryCore.frameworkLibrary.113053
- _VoiceShortcutClientLibraryCore.frameworkLibrary.123612
- ___32-[INImageServiceConnection init]_block_invoke.2
- ___77-[INImageServiceConnection fetchShareExtensionIntentForExtensionContextUUID:]_block_invoke.70
- ___79-[INImageServiceConnection storeImage:scaled:qualityOfService:storeType:error:]_block_invoke.75
- ___97-[_INURLImage(INPortableImageLoader) _loadImageDataAndSizeWithHelper:accessSpecifier:completion:]_block_invoke.120
- ___97-[_INURLImage(INPortableImageLoader) _loadImageDataAndSizeWithHelper:accessSpecifier:completion:]_block_invoke.122
- ___97-[_INURLImage(INPortableImageLoader) _loadImageDataAndSizeWithHelper:accessSpecifier:completion:]_block_invoke.126
- ___Block_byref_object_copy_.100539
- ___Block_byref_object_copy_.104505
- ___Block_byref_object_copy_.68263
- ___Block_byref_object_copy_.69072
- ___Block_byref_object_copy_.71933
- ___Block_byref_object_copy_.75146
- ___Block_byref_object_copy_.90463
- ___Block_byref_object_dispose_.100540
- ___Block_byref_object_dispose_.104506
- ___Block_byref_object_dispose_.68264
- ___Block_byref_object_dispose_.69073
- ___Block_byref_object_dispose_.71934
- ___Block_byref_object_dispose_.75147
- ___Block_byref_object_dispose_.90464
- ___ChronoServicesLibraryCore_block_invoke.123690
- ___ContactsLibraryCore_block_invoke.111119
- ___CoreGraphicsLibraryCore_block_invoke.136732
- ___CoreSpotlightLibraryCore_block_invoke.79785
- ___HealthKitLibraryCore_block_invoke.95496
- ___IntentsUILibraryCore_block_invoke.83658
- ___LinkServicesLibraryCore_block_invoke.166035
- ___VoiceShortcutClientLibraryCore_block_invoke.113054
- ___VoiceShortcutClientLibraryCore_block_invoke.123613
- ___block_literal_global.10.103471
- ___block_literal_global.100285
- ___block_literal_global.100460
- ___block_literal_global.103461
- ___block_literal_global.104606
- ___block_literal_global.105622
- ___block_literal_global.11.111762
- ___block_literal_global.111790
- ___block_literal_global.119896
- ___block_literal_global.12.158312
- ___block_literal_global.123712
- ___block_literal_global.13.103473
- ___block_literal_global.13.98773
- ___block_literal_global.158300
- ___block_literal_global.3.111761
- ___block_literal_global.5.94150
- ___block_literal_global.58
- ___block_literal_global.6.111773
- ___block_literal_global.6.72049
- ___block_literal_global.62
- ___block_literal_global.68338
- ___block_literal_global.68455
- ___block_literal_global.69
- ___block_literal_global.69074
- ___block_literal_global.70477
- ___block_literal_global.71239
- ___block_literal_global.71983
- ___block_literal_global.72045
- ___block_literal_global.75006
- ___block_literal_global.77371
- ___block_literal_global.82380
- ___block_literal_global.91.71984
- ___block_literal_global.91431
- ___block_literal_global.92290
- ___block_literal_global.94174
- ___block_literal_global.98784
- ___getCGColorCreateSRGBSymbolLoc_block_invoke.136777
- ___getCGColorGetComponentsSymbolLoc_block_invoke.136725
- ___getCNPostalAddressClass_block_invoke.111117
- ___getCSSearchableItemAttributeSetClass_block_invoke.79783
- ___getHKUnitClass_block_invoke.95494
- _audit_stringChronoServices.123695
- _audit_stringContacts.111124
- _audit_stringCoreGraphics.136734
- _audit_stringCoreSpotlight.79790
- _audit_stringHealthKit.95501
- _audit_stringLinkServices.166040
- _audit_stringVoiceShortcutClient.113059
- _audit_stringVoiceShortcutClient.123618
- _getCGColorCreateSRGBSymbolLoc.ptr.136776
- _getCGColorGetComponentsSymbolLoc.ptr.136724
- _getCNPostalAddressClass.softClass.111116
- _getCSSearchableItemAttributeSetClass.softClass.79782
- _getHKUnitClass.95492
- _getHKUnitClass.softClass.95493
- _intentDescription.intentDescription.68456
- _intentDescription.onceToken.68454
- _objc_msgSend$accessSpecifierFilteredForAssociatedAppBundleIdentifier:
- _objc_msgSend$initWithAccessLevel:associatedAppBundleIdentifier:
- _serviceIdentifier.onceToken.83631
- _serviceIdentifier.sServiceIdentifier.83632
- _sharedCache.onceToken.82379
- _sharedManager.onceToken.123711
- _sharedManager.sharedManager.123713
- _sharedProvider.onceToken.158311
CStrings:
+ "%s Copied URL image failed validation at %@: %@"
+ "%s File URL access validation failed for %@: %@. Accesing security scoped resource: %d"
+ "%s Image validation successful for %@"
+ "%s Source URL image failed validation at %@: %@"
+ "%s Source URL image validation successful at %@"
+ "%s URL image failed validation at %@: %@"
+ "%s URL image validation successful at %@"
+ "@40@0:8Q16@24@32"
+ "Access to file path outside of sandbox not permitted."
+ "B40@0:8@16@24^@32"
+ "File does not appear to be a valid image format"
+ "No valid image data found"
+ "Service access denied - missing or invalid audit token"
+ "Service access denied - no access level"
+ "T@\"NSData\",R,C,N,V_associatedAuditToken"
+ "Unable to read image properties - invalid image data"
+ "_validateFileURLAccess:accessSpecifier:error:"
+ "_validateFileURLAccess:error:"
+ "_validateImageData:error:"
+ "accessSpecifierFilteredForAssociatedAppBundleIdentifier:auditToken:"
+ "associatedAuditToken"
+ "dataWithContentsOfURL:"
+ "file-read-data"
+ "initWithAccessLevel:associatedAppBundleIdentifier:auditToken:"
+ "initWithBytes:length:"
- "accessSpecifierFilteredForAssociatedAppBundleIdentifier:"
- "initWithAccessLevel:associatedAppBundleIdentifier:"

```
