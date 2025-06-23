## AppPredictionFoundation

> `/System/Library/PrivateFrameworks/AppPredictionFoundation.framework/AppPredictionFoundation`

```diff

-610.0.11.0.0
-  __TEXT.__text: 0x19da8
+613.0.1.0.0
+  __TEXT.__text: 0x1aac4
   __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__objc_methlist: 0x18a4
-  __TEXT.__const: 0x418
+  __TEXT.__objc_methlist: 0x1974
+  __TEXT.__const: 0x420
   __TEXT.__gcc_except_tab: 0x3dc
-  __TEXT.__cstring: 0x2048
-  __TEXT.__oslogstring: 0x1ad3
-  __TEXT.__unwind_info: 0x7d8
-  __TEXT.__objc_classname: 0x47a
-  __TEXT.__objc_methname: 0x44ff
-  __TEXT.__objc_methtype: 0x894
-  __TEXT.__objc_stubs: 0x2f40
-  __DATA_CONST.__got: 0x288
+  __TEXT.__cstring: 0x20bb
+  __TEXT.__oslogstring: 0x1b82
+  __TEXT.__unwind_info: 0x818
+  __TEXT.__objc_classname: 0x498
+  __TEXT.__objc_methname: 0x46fe
+  __TEXT.__objc_methtype: 0x8b1
+  __TEXT.__objc_stubs: 0x3020
+  __DATA_CONST.__got: 0x298
   __DATA_CONST.__const: 0xaf8
-  __DATA_CONST.__objc_classlist: 0x140
+  __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1100
+  __DATA_CONST.__objc_selrefs: 0x1140
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xb0
+  __DATA_CONST.__objc_superrefs: 0xb8
   __AUTH_CONST.__auth_got: 0x370
   __AUTH_CONST.__const: 0x8e0
-  __AUTH_CONST.__cfstring: 0x1fa0
-  __AUTH_CONST.__objc_const: 0x6f28
+  __AUTH_CONST.__cfstring: 0x2080
+  __AUTH_CONST.__objc_const: 0x71f8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x870
-  __DATA.__objc_ivar: 0x158
+  __AUTH.__objc_data: 0x8c0
+  __DATA.__objc_ivar: 0x174
   __DATA.__data: 0x360
   __DATA.__bss: 0x2e8
   __DATA_DIRTY.__objc_data: 0x410

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FEA2EFF0-9A55-31EF-83DA-EF70E89CAD25
-  Functions: 825
-  Symbols:   3061
-  CStrings:  1562
+  UUID: 35D548AE-49F6-363B-AF5A-B63E2DA4311D
+  Functions: 845
+  Symbols:   3136
+  CStrings:  1599
 
Symbols:
+ +[ATXFileIdentityWithMetadata supportsSecureCoding]
+ +[ATXUtils isInTrashPath:]
+ +[ATXUtils isInTrashPath:].cold.1
+ -[ATXDocumentInteractionEvent bundleIdentifier]
+ -[ATXDocumentInteractionEvent initWithInteractionType:originalFileURL:bookmarkData:isRemote:bundleIdentifier:]
+ -[ATXFileIdentityWithMetadata .cxx_destruct]
+ -[ATXFileIdentityWithMetadata bookmarkData]
+ -[ATXFileIdentityWithMetadata bundleIdentifier]
+ -[ATXFileIdentityWithMetadata copyWithZone:]
+ -[ATXFileIdentityWithMetadata dateCreated]
+ -[ATXFileIdentityWithMetadata dateLastOpened]
+ -[ATXFileIdentityWithMetadata dateModified]
+ -[ATXFileIdentityWithMetadata encodeWithCoder:]
+ -[ATXFileIdentityWithMetadata hash]
+ -[ATXFileIdentityWithMetadata initWithCoder:]
+ -[ATXFileIdentityWithMetadata initWithItemURL:bookmarkData:dateLastOpened:dateModified:dateCreated:bundleIdentifier:]
+ -[ATXFileIdentityWithMetadata isEqual:]
+ -[ATXFileIdentityWithMetadata isEqualToATXFileIdentityWithMetadata:]
+ -[ATXFileIdentityWithMetadata itemURL]
+ -[ATXFileIdentityWithMetadata resolveItemURLWithError:]
+ _NSFileCreationDate
+ _OBJC_CLASS_$_ATXFileIdentityWithMetadata
+ _OBJC_IVAR_$_ATXDocumentInteractionEvent._bundleIdentifier
+ _OBJC_IVAR_$_ATXFileIdentityWithMetadata._bookmarkData
+ _OBJC_IVAR_$_ATXFileIdentityWithMetadata._bundleIdentifier
+ _OBJC_IVAR_$_ATXFileIdentityWithMetadata._dateCreated
+ _OBJC_IVAR_$_ATXFileIdentityWithMetadata._dateLastOpened
+ _OBJC_IVAR_$_ATXFileIdentityWithMetadata._dateModified
+ _OBJC_IVAR_$_ATXFileIdentityWithMetadata._itemURL
+ _OBJC_METACLASS_$_ATXFileIdentityWithMetadata
+ __OBJC_$_CLASS_METHODS_ATXFileIdentityWithMetadata
+ __OBJC_$_CLASS_PROP_LIST_ATXFileIdentityWithMetadata
+ __OBJC_$_INSTANCE_METHODS_ATXFileIdentityWithMetadata
+ __OBJC_$_INSTANCE_VARIABLES_ATXFileIdentityWithMetadata
+ __OBJC_$_PROP_LIST_ATXFileIdentityWithMetadata
+ __OBJC_CLASS_PROTOCOLS_$_ATXFileIdentityWithMetadata
+ __OBJC_CLASS_RO_$_ATXFileIdentityWithMetadata
+ __OBJC_METACLASS_RO_$_ATXFileIdentityWithMetadata
+ ___61-[ATXDocumentInteractionStream getDocumentsOpenedInLastMonth]_block_invoke_3.cold.1
+ ___61-[ATXDocumentInteractionStream getDocumentsOpenedInLastMonth]_block_invoke_3.cold.2
+ ___block_descriptor_40_e8_32s_e34_v32?0"NSURL"8"_PASTuple2"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e48_v24?0"ATXDocumentInteractionEvent"8"NSDate"16ls32l8
+ _objc_msgSend$URLByResolvingBookmarkData:options:relativeToURL:bookmarkDataIsStale:error:
+ _objc_msgSend$atx_errorWithCode:debugDescription:
+ _objc_msgSend$date
+ _objc_msgSend$getRelationship:ofDirectory:inDomain:toItemAtURL:error:
+ _objc_msgSend$initWithInteractionType:originalFileURL:bookmarkData:isRemote:bundleIdentifier:
+ _objc_msgSend$initWithItemURL:bookmarkData:dateLastOpened:dateModified:dateCreated:bundleIdentifier:
+ _objc_msgSend$isEqualToATXFileIdentityWithMetadata:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$resolveItemURLWithError:
- +[ATXFeatureFlags isSpotlightPlusInternalToolKitInvocationsEnabled]
- +[ATXFeatureFlags isSpotlightPlusModelDevelopmentEnabled]
- -[ATXDocumentInteractionEvent initWithInteractionType:originalFileURL:bookmarkData:isRemote:]
- ___block_descriptor_40_e8_32s_e30_v32?0"NSURL"8"NSData"16^B24ls32l8
- ___block_descriptor_40_e8_32s_e37_v16?0"ATXDocumentInteractionEvent"8ls32l8
- _objc_msgSend$bundleURL
- _objc_msgSend$initWithInteractionType:originalFileURL:bookmarkData:isRemote:
CStrings:
+ "@48@0:8i16@20@28B36@40"
+ "@64@0:8@16@24@32@40@48@56"
+ "ATXFileIdentityWithMetadata"
+ "Bookmark data is nil."
+ "Document Interaction - Empty appIdentity or missing bundle identifier"
+ "Error retrieving relationship of %{sensitive}@ to Trash folder: %@"
+ "Failed to get attributes for file %@: %@"
+ "Failed to resolve bookmark for URL %@, falling back to original url: %@"
+ "T@\"NSDate\",R,C,N,V_dateCreated"
+ "T@\"NSDate\",R,C,N,V_dateLastOpened"
+ "T@\"NSDate\",R,C,N,V_dateModified"
+ "T@\"NSString\",R,N,V_bundleIdentifier"
+ "T@\"NSURL\",R,C,N,V_itemURL"
+ "URLByResolvingBookmarkData:options:relativeToURL:bookmarkDataIsStale:error:"
+ "_bundleIdentifier"
+ "_dateCreated"
+ "_dateLastOpened"
+ "_dateModified"
+ "_itemURL"
+ "date"
+ "dateCreated"
+ "dateLastOpened"
+ "dateModified"
+ "getRelationship:ofDirectory:inDomain:toItemAtURL:error:"
+ "initWithInteractionType:originalFileURL:bookmarkData:isRemote:bundleIdentifier:"
+ "initWithItemURL:bookmarkData:dateLastOpened:dateModified:dateCreated:bundleIdentifier:"
+ "isEqualToATXFileIdentityWithMetadata:"
+ "isInTrashPath:"
+ "localizedDescription"
+ "resolveItemURLWithError:"
+ "v24@?0@\"ATXDocumentInteractionEvent\"8@\"NSDate\"16"
+ "v32@?0@\"NSURL\"8@\"_PASTuple2\"16^B24"
- "@40@0:8i16@20@28B36"
- "Document Interaction - Empty appIdentity or missing bundle identifier/path"
- "bundleURL"
- "initWithInteractionType:originalFileURL:bookmarkData:isRemote:"
- "isSpotlightPlusInternalToolKitInvocationsEnabled"
- "isSpotlightPlusModelDevelopmentEnabled"
- "v16@?0@\"ATXDocumentInteractionEvent\"8"
- "v32@?0@\"NSURL\"8@\"NSData\"16^B24"

```
