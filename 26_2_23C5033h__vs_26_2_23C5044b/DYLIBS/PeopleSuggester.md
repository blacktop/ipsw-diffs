## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester`

```diff

-1924.9.0.0.0
+1924.10.0.0.0
   __TEXT.__text: 0xef884
   __TEXT.__auth_stubs: 0xf90
   __TEXT.__objc_methlist: 0x9964
   __TEXT.__const: 0x8b8
   __TEXT.__gcc_except_tab: 0x2e68
-  __TEXT.__cstring: 0xb149
-  __TEXT.__oslogstring: 0xba0e
+  __TEXT.__cstring: 0xae29
+  __TEXT.__oslogstring: 0xba7f
   __TEXT.__dlopen_cstrs: 0x17f0
   __TEXT.__ustring: 0x33e
   __TEXT.__unwind_info: 0x2ac0
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x1146
-  __TEXT.__objc_methname: 0x215d8
+  __TEXT.__objc_methname: 0x21633
   __TEXT.__objc_methtype: 0x26d8
-  __TEXT.__objc_stubs: 0x12c60
-  __DATA_CONST.__got: 0x8e8
+  __TEXT.__objc_stubs: 0x12ca0
+  __DATA_CONST.__got: 0x8e0
   __DATA_CONST.__const: 0x3718
   __DATA_CONST.__objc_classlist: 0x4c0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x63a8
+  __DATA_CONST.__objc_selrefs: 0x63c0
   __DATA_CONST.__objc_superrefs: 0x388
   __DATA_CONST.__objc_arraydata: 0xcb8
   __AUTH_CONST.__auth_got: 0x7d8
   __AUTH_CONST.__const: 0x19c0
-  __AUTH_CONST.__cfstring: 0xbb40
+  __AUTH_CONST.__cfstring: 0xbb00
   __AUTH_CONST.__objc_const: 0x12dc0
   __AUTH_CONST.__objc_intobj: 0x1128
   __AUTH_CONST.__objc_arrayobj: 0x828

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7283262E-99D4-370A-BC28-F188D2BA3A38
-  Functions: 4562
-  Symbols:   15950
-  CStrings:  9190
+  UUID: 24CC0DF5-EA1A-3F01-A83E-FC136B06A6E0
+  Functions: 4561
+  Symbols:   15949
+  CStrings:  9189
 
Symbols:
+ -[_PSContactHandleFeatureProvider _interactionFeaturesForHandle:store:]
+ -[_PSContactHandleFeatureProvider _interactionFeaturesForHandle:store:].cold.1
+ ___64-[_PSContactHandleFeatureProvider interactionFeaturesForHandle:]_block_invoke.22
+ _objc_msgSend$incomingSenderCount
+ _objc_msgSend$lastIncomingSenderDate
+ _objc_msgSend$lastOutgoingRecipientDate
+ _objc_msgSend$laterDate:
+ _objc_msgSend$outgoingRecipientCount
+ _objc_msgSend$queryContactsUsingPredicate:sortDescriptors:limit:error:
+ _objc_msgSend$statistics
- -[_PSContactHandleFeatureProvider _interactionFeaturesForHandle:]
- -[_PSContactHandleFeatureProvider _interactionFeaturesForHandle:].cold.1
- -[_PSContactHandleFeatureProvider _interactionFeaturesForHandle:].cold.2
- _OBJC_CLASS_$_BMSQLDatabase
- ___64-[_PSContactHandleFeatureProvider interactionFeaturesForHandle:]_block_invoke.16
- _objc_msgSend$executeQuery:
- _objc_msgSend$featureNames
- _objc_msgSend$next
- _objc_msgSend$row
- _objc_msgSend$stringByReplacingOccurrencesOfString:withString:options:range:
CStrings:
+ "Error querying interactions database (_interactionFeaturesForHandle:%{private}@): %@"
+ "_PSContactHandleFeatureProvider Getting interaction features for handle: %@"
+ "_interactionFeaturesForHandle:store:"
+ "identifier == %@"
+ "incomingSenderCount"
+ "lastIncomingSenderDate"
+ "lastOutgoingRecipientDate"
+ "laterDate:"
+ "outgoingRecipientCount"
+ "queryContactsUsingPredicate:sortDescriptors:limit:error:"
+ "statistics"
- "'"
- "''"
- "Error getting features for handle %@"
- "SELECT    intentClass,    bundleId,    groupIdentifier,    COALESCE(%d - MAX(CASE WHEN interactionDirection = 2 THEN absoluteTimestamp END), -1) AS %@,    COALESCE(%d - MAX(CASE WHEN interactionDirection = 3 THEN absoluteTimestamp END), -1) AS %@,    COUNT(CASE WHEN interactionDirection = 2 THEN 1 END) AS %@,    COUNT(CASE WHEN interactionDirection = 3 THEN 1 END) AS %@ FROM    \"App.Intent\" WHERE\n    (intentClass = 'INSendMessageIntent'    AND groupIdentifier = 'iMessage;-;%@') OR (intentClass = 'INSendMessageIntent'    AND groupIdentifier = 'SMS;-;%@') OR (intentClass = 'INSendMessageIntent'    AND groupIdentifier = 'RCS;-;%@') OR (intentClass = 'INSendMessageIntent'    AND groupIdentifier = 'any;-;%@') OR (intentClass = 'INStartCallIntent'    AND groupIdentifier = '%@') GROUP BY    groupIdentifier;"
- "_interactionFeaturesForHandle:"
- "executeQuery:"
- "next"
- "query = %@"
- "row"
- "stringByReplacingOccurrencesOfString:withString:options:range:"

```
