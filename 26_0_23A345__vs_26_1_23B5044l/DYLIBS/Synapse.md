## Synapse

> `/System/Library/PrivateFrameworks/Synapse.framework/Synapse`

```diff

-144.0.0.0.0
-  __TEXT.__text: 0x39864
+145.0.0.0.0
+  __TEXT.__text: 0x3968c
   __TEXT.__auth_stubs: 0x710
   __TEXT.__objc_methlist: 0x325c
-  __TEXT.__const: 0x160
-  __TEXT.__gcc_except_tab: 0xc64
-  __TEXT.__cstring: 0x2e96
-  __TEXT.__oslogstring: 0x441e
-  __TEXT.__dlopen_cstrs: 0x502
+  __TEXT.__const: 0x158
+  __TEXT.__gcc_except_tab: 0xc74
+  __TEXT.__cstring: 0x2ee8
+  __TEXT.__oslogstring: 0x43c7
+  __TEXT.__dlopen_cstrs: 0x558
   __TEXT.__ustring: 0x154
   __TEXT.__unwind_info: 0x1218
   __TEXT.__objc_classname: 0xb89

   __TEXT.__objc_methtype: 0x1378
   __TEXT.__objc_stubs: 0x5c00
   __DATA_CONST.__got: 0x378
-  __DATA_CONST.__const: 0x14c8
+  __DATA_CONST.__const: 0x14e0
   __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf0

   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x398
   __AUTH_CONST.__const: 0x420
-  __AUTH_CONST.__cfstring: 0x2440
+  __AUTH_CONST.__cfstring: 0x2460
   __AUTH_CONST.__objc_const: 0xdbb8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x2bc
   __DATA.__data: 0xb40
-  __DATA.__bss: 0x191
+  __DATA.__bss: 0x1a1
   __DATA_DIRTY.__objc_data: 0x1450
   __DATA_DIRTY.__data: 0x1
   __DATA_DIRTY.__bss: 0xf8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1CEE6413-6162-30CD-BBE4-33D7C318D899
-  Functions: 1490
-  Symbols:   5536
-  CStrings:  2521
+  UUID: 4EB23B8F-091E-3F48-AC4A-00F32F4D2916
+  Functions: 1471
+  Symbols:   5486
+  CStrings:  2524
 
Symbols:
+ +[SYFileExtendedAttributes fetchPrivateAttributesForFileURL:completion:].cold.1
+ _MobileKeyBagLibraryCore.frameworkLibrary
+ _SYIsDeviceLocked
+ _SYIsDeviceLocked.cold.1
+ _SYPathIsInUserLibrarySubdirectory
+ ___55-[SYDocumentWorkflowsClient performRequest:completion:]_block_invoke.33
+ ___55-[SYDocumentWorkflowsClient performRequest:completion:]_block_invoke_2.34
+ ___55-[SYDocumentWorkflowsClient performRequest:completion:]_block_invoke_2.34.cold.1
+ ___57-[SYDocumentWorkflowsClient _createConnectionIfNecessary]_block_invoke.126
+ ___71+[SYFileExtendedAttributes setPrivateAttributes:forFileURL:completion:]_block_invoke.cold.1
+ ___72-[SYDocumentWorkflowsClient hasOriginalDocumentForFileAtURL:completion:]_block_invoke.37
+ ___73-[SYDocumentWorkflowsClient openOriginalDocumentForFileAtURL:completion:]_block_invoke.40
+ ___76-[SYDocumentWorkflowsClient hasLastModifiedDocumentForFileAtURL:completion:]_block_invoke.43
+ ___77-[SYDocumentWorkflowsClient openLastModifiedDocumentForFileAtURL:completion:]_block_invoke.45
+ ___81-[SYDocumentWorkflowsClient fetchAttributesForDocumentsWithIndexKeys:completion:]_block_invoke_3
+ ___MobileKeyBagLibraryCore_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls40l8s32l8
+ ___getMKBGetDeviceLockStateSymbolLoc_block_invoke
+ ___getMKBGetDeviceLockStateSymbolLoc_block_invoke.cold.1
+ _audit_stringMobileKeyBag
+ _getMKBGetDeviceLockStateSymbolLoc.ptr
- +[SYDocumentAttributes(Writing) _removeDocumentAttributesForFileAtURL:keepDocumentRelatedUniqueIdentifierKey:error:].cold.1
- +[SYDocumentAttributesFetchRequest _buildResultWithMatches:].cold.1
- +[SYDocumentWorkflowsContentType isImageContentType:].cold.1
- +[SYFormFillingDocumentAttributes formFillingDocumentAttributesForFileAtURL:completion:].cold.2
- +[SYFormFillingDocumentAttributes formFillingDocumentAttributesForFileAtURL:error:].cold.1
- +[SYFormFillingDocumentAttributes removeFormFillingDocumentAttributesForFileAtURL:error:].cold.1
- -[SYDocumentSender formattedNameWithStyle:].cold.1
- -[SYDocumentSender formattedNameWithStyle:].cold.2
- -[SYDocumentSenderAvatar _renderAvatarImageWithRenderer:renderingScope:].cold.1
- -[SYDocumentWorkflowsClient canPerformRequest:completion:].cold.1
- -[SYDocumentWorkflowsClient canPerformRequest:completion:].cold.2
- -[SYDocumentWorkflowsClient canPerformRequest:completion:].cold.3
- -[SYDocumentWorkflowsClient fetchAttributesForDocumentsWithIndexKeys:completion:].cold.1
- -[SYDocumentWorkflowsClient fetchAttributesForDocumentsWithIndexKeys:completion:].cold.2
- -[SYDocumentWorkflowsCoreDataStore fetchUserActivityWithRelatedUniqueIdentifier:error:].cold.1
- -[SYReturnToDocumentRequest verifyParameters].cold.1
- _SYPathIsInMailDownloadsDir
- ___55-[SYDocumentWorkflowsClient performRequest:completion:]_block_invoke.34
- ___55-[SYDocumentWorkflowsClient performRequest:completion:]_block_invoke_2.35
- ___55-[SYDocumentWorkflowsClient performRequest:completion:]_block_invoke_2.35.cold.1
- ___57-[SYDocumentWorkflowsClient _createConnectionIfNecessary]_block_invoke.127
- ___60-[SYDocumentWorkflowsClient _dispatchRequestWithCompletion:]_block_invoke.cold.1
- ___72-[SYDocumentWorkflowsClient hasOriginalDocumentForFileAtURL:completion:]_block_invoke.39
- ___73-[SYDocumentWorkflowsClient openOriginalDocumentForFileAtURL:completion:]_block_invoke.41
- ___76-[SYDocumentWorkflowsClient hasLastModifiedDocumentForFileAtURL:completion:]_block_invoke.45
- ___77-[SYDocumentWorkflowsClient openLastModifiedDocumentForFileAtURL:completion:]_block_invoke.47
- ___80+[SYDocumentAttributes(Reading) fetchDocumentAttributesForFileAtURL:completion:]_block_invoke_2.cold.1
- ___80+[SYDocumentAttributes(Reading) fetchDocumentAttributesForFileAtURL:completion:]_block_invoke_2.cold.2
- ___80+[SYDocumentAttributes(Reading) fetchDocumentAttributesForFileAtURL:completion:]_block_invoke_2.cold.3
- ___80+[SYDocumentAttributes(Reading) fetchDocumentAttributesForFileAtURL:completion:]_block_invoke_2.cold.4
- ___80+[SYDocumentAttributes(Reading) fetchDocumentAttributesForFileAtURL:completion:]_block_invoke_2.cold.5
- ___81-[SYDocumentWorkflowsClient fetchAttributesForDocumentsWithIndexKeys:completion:]_block_invoke.26
- ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
CStrings:
+ "Device is locked, skipping LP preview for item: %@"
+ "Device is locked, skipping icon preview for item: %@"
+ "MKBGetDeviceLockState"
+ "Mail/AttachmentData/"
+ "SYCommon.m"
+ "Searchable item isn't valid: %@, reason: %@"
+ "Unable to set private attributes for url path: %{private}@, error: %@"
+ "error fetching private attributes for url path: %{private}@, attrs: %{private}@, error: %@"
+ "int __MKBGetDeviceLockState(CFDictionaryRef)"
+ "softlink:r:path:/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag"
+ "void *MobileKeyBagLibrary(void)"
- "/private/var/mobile/Library/Mail/AttachmentData/"
- "Finished fetching private attributes for url path: %{private}@, attrs: %{private}@, error: %@"
- "Finished setting private attributes for url path: %{private}@, error: %@"
- "No private attributes at URL: %@, error: %@"
- "No private attributes at URL: %{public}@, error: %@"
- "No private attributes data at URL: %@, error: %@"
- "Unsupported request type."
- "completion can't be nil."
- "indexKeys can't be nil or empty."

```
