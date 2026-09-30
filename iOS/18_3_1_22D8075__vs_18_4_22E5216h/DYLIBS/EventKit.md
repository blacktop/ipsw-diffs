## EventKit

> `/System/Library/Frameworks/EventKit.framework/EventKit`

```diff

-1902.3.1.100.0
-  __TEXT.__text: 0x1316c8
-  __TEXT.__auth_stubs: 0x14d0
-  __TEXT.__objc_methlist: 0x13928
-  __TEXT.__const: 0x5f2
-  __TEXT.__cstring: 0xaf14
-  __TEXT.__oslogstring: 0xd2ae
-  __TEXT.__gcc_except_tab: 0x361c
+1902.5.5.0.0
+  __TEXT.__text: 0x133368
+  __TEXT.__auth_stubs: 0x1460
+  __TEXT.__objc_methlist: 0x14804
+  __TEXT.__const: 0x602
+  __TEXT.__cstring: 0xaca2
+  __TEXT.__oslogstring: 0xd3ae
+  __TEXT.__gcc_except_tab: 0x364c
   __TEXT.__dlopen_cstrs: 0x30e
   __TEXT.__ustring: 0x162
   __TEXT.__constg_swiftt: 0xfc
-  __TEXT.__swift5_typeref: 0x267
+  __TEXT.__swift5_typeref: 0x253
   __TEXT.__swift5_reflstr: 0x1b2
   __TEXT.__swift5_fieldmd: 0xe8
   __TEXT.__swift5_capture: 0x140
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x4cf8
+  __TEXT.__unwind_info: 0x4eb0
   __TEXT.__objc_classname: 0x18c3
-  __TEXT.__objc_methname: 0x2bf52
-  __TEXT.__objc_methtype: 0x406f
-  __TEXT.__objc_stubs: 0x1f420
-  __DATA_CONST.__got: 0x1600
-  __DATA_CONST.__const: 0x40c8
+  __TEXT.__objc_methname: 0x2c2a1
+  __TEXT.__objc_methtype: 0x4080
+  __TEXT.__objc_stubs: 0x1f620
+  __DATA_CONST.__got: 0x1610
+  __DATA_CONST.__const: 0x4120
   __DATA_CONST.__objc_classlist: 0x6e0
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa200
+  __DATA_CONST.__objc_selrefs: 0xa358
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x4e0
   __DATA_CONST.__objc_arraydata: 0x5c0
-  __AUTH_CONST.__auth_got: 0xa78
+  __AUTH_CONST.__auth_got: 0xa40
   __AUTH_CONST.__auth_ptr: 0x38
-  __AUTH_CONST.__const: 0x1ea0
+  __AUTH_CONST.__const: 0x1ec0
   __AUTH_CONST.__cfstring: 0x93c0
-  __AUTH_CONST.__objc_const: 0x17378
+  __AUTH_CONST.__objc_const: 0x15a70
   __AUTH_CONST.__objc_intobj: 0x678
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_doubleobj: 0x100
   __AUTH.__objc_data: 0x25b8
   __AUTH.__data: 0xa8
-  __DATA.__objc_ivar: 0xbe8
-  __DATA.__data: 0x1640
-  __DATA.__bss: 0x3c0
+  __DATA.__objc_ivar: 0xbf0
+  __DATA.__data: 0x1630
+  __DATA.__bss: 0x410
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x2120
   __DATA_DIRTY.__data: 0x18
-  __DATA_DIRTY.__bss: 0x8e0
+  __DATA_DIRTY.__bss: 0x890
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8273
-  Symbols:   9598
-  CStrings:  9666
+  Functions: 8455
+  Symbols:   9801
+  CStrings:  9679
 
Symbols:
+ _EKAttachmentProperty_URLWrapperForPendingFileCopy
+ _OBJC_CLASS_$_CalMockPreferenceStore
+ _OBJC_CLASS_$_CalOpenFileURLWrapper
- _EKAttachmentProperty_securityScopedURLWrapperForPendingFileCopy
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
CStrings:
+ "\x02\x11)"
+ "\x0f\x06\x1322\x1f\r"
+ "@\"EKPreferences\""
+ "@\"NSArray\"24@?0@\"EKObject\"8@\"EKObject\"16"
+ "Attempted to set URL on an alarm on a platform that does not support this. Ignoring."
+ "Error creating archive of %@: %@"
+ "Found event that should have had the identifier %@ using the identifier %@ instead. Pretending that these are the same thing."
+ "T@\"EKPreferences\",R,N,V_preferences"
+ "T@\"NSString\",&,N,V_appEntityIdentifierOverride"
+ "URLWrapperForPendingFileCopy"
+ "Unable to determine if %@ is a file or directory: %@"
+ "_appEntityIdentifierOverride"
+ "_compressItemAtURLToTemporaryDirectory:"
+ "_multiValueRelatedObject:isAlsoASingleValueRelatedObjectForKey:"
+ "_populateIdentityKeysForDiff:keysToIgnore:"
+ "_populateImmutableKeysForDiff:keysToIgnore:"
+ "_populateMultiValueRelationshipKeysForDiff:keysToIgnore:fetchKeysToIgnoreBlock:"
+ "_populateSingleValueKeysForDiff:keysToIgnore:fetchKeysToIgnoreBlock:"
+ "_populateSingleValueRelationshipKeysForDiff:keysToIgnore:fetchKeysToIgnoreBlock:"
+ "_prepareFileAtURLInTemporaryDirectory:"
+ "_processIsAllowedToCreateProcedureAlarms"
+ "appEntityIdentifier"
+ "appEntityIdentifierOverride"
+ "archiveURLToFile:toFile:createPKZipArchive:error:"
+ "currentProcessIsFirstPartyApp"
+ "diffBetweenObject:andObject:fetchKeysToIgnoreBlock:"
+ "eventWithAppEntityIdentifier:"
+ "eventWithRecurrenceIdentifier:isAppEntityID:"
+ "initWithDomain:store:"
+ "initWithPreferences:"
+ "keysToIgnoreForComparingUIVisiblePropertiesOfObject:andObject:"
+ "preferences"
+ "preferencesStoreForPath:"
+ "primitiveSetURLWrapperValue:forKey:"
+ "primitiveURLWrapperValueForKey:"
+ "setAppEntityIdentifierOverride:"
+ "setURLWrapperForPendingFileCopy:"
+ "uniqueIDForDetachedOccurrenceOfEvent:withOriginalStartDate:timeZone:allDay:"
+ "zip"
- "\x02\x11("
- "\x0f\x06\x1322\x1f\f"
- "%@/RID=%lu"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Single value relationship differences? [%d] - %@"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_copyFileAtURLToTemporaryDirectory:"
- "_populateIdentityKeysForDiff:"
- "_populateImmutableKeysForDiff:"
- "_populateMultiValueRelationshipKeysForDiff:compareUIVisiblePropertiesOnly:"
- "_populateSingleValueKeysForDiff:compareUIVisiblePropertiesOnly:"
- "_populateSingleValueRelationshipKeysForDiff:compareUIVisiblePropertiesOnly:"
- "invalid Collection: less than 'count' elements in collection"
- "securityScopedURLWrapperForPendingFileCopy"
- "setSecurityScopedURLWrapperForPendingFileCopy:"

```
