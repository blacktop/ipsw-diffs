## XCTAutomationSupport

> `/System/Library/PrivateFrameworks/XCTAutomationSupport.framework/Versions/A/XCTAutomationSupport`

```diff

-23196.3.0.0.0
-  __TEXT.__text: 0x35c30
+23790.0.0.0.0
+  __TEXT.__text: 0x368a8
   __TEXT.__auth_stubs: 0xb80
-  __TEXT.__objc_methlist: 0x2d34
+  __TEXT.__objc_methlist: 0x32f8
   __TEXT.__const: 0x63e
-  __TEXT.__cstring: 0x83e9
-  __TEXT.__oslogstring: 0x2af1
-  __TEXT.__gcc_except_tab: 0x984
+  __TEXT.__cstring: 0x84c9
+  __TEXT.__oslogstring: 0x2b9e
+  __TEXT.__gcc_except_tab: 0x998
   __TEXT.__ustring: 0x132
   __TEXT.__swift5_typeref: 0x79
   __TEXT.__constg_swiftt: 0x38

   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xc58
-  __TEXT.__objc_classname: 0x87e
-  __TEXT.__objc_methname: 0x73e0
+  __TEXT.__unwind_info: 0xcc8
+  __TEXT.__objc_classname: 0x895
+  __TEXT.__objc_methname: 0x7432
   __TEXT.__objc_methtype: 0x15e0
-  __TEXT.__objc_stubs: 0x5380
+  __TEXT.__objc_stubs: 0x53e0
   __DATA_CONST.__got: 0x6f8
   __DATA_CONST.__const: 0x608
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18b0
+  __DATA_CONST.__objc_selrefs: 0x1958
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0xa48
   __AUTH_CONST.__auth_got: 0x5d0
   __AUTH_CONST.__const: 0xa58
-  __AUTH_CONST.__cfstring: 0x83a0
-  __AUTH_CONST.__objc_const: 0x9a00
+  __AUTH_CONST.__cfstring: 0x8460
+  __AUTH_CONST.__objc_const: 0x9030
   __AUTH_CONST.__objc_intobj: 0xa50
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x50

   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 74750752-2412-3F7B-82F2-CC8B9F1A8B29
-  Functions: 1176
-  Symbols:   3712
-  CStrings:  3843
+  UUID: 17E97ABF-316F-3E6E-8EF8-E04E7FC5F009
+  Functions: 1241
+  Symbols:   3783
+  CStrings:  3861
 
Symbols:
+ +[XCElementSnapshot(XCUITypeIdentification) utIdentifierString]
+ +[XCTRuntimeIssueContext aggregationOfRuntimeIssues:].cold.1
+ -[XCAXCycleDetector untrackElement:].cold.1
+ -[XCElementSnapshot _faultingBitForKey:].cold.1
+ -[XCElementSnapshot _fetchPrivilegedValueForKey:].cold.1
+ -[XCElementSnapshot _fetchPrivilegedValueForKey:].cold.2
+ -[XCElementSnapshot _fetchPrivilegedValueForKey:].cold.3
+ -[XCElementSnapshot _fetchSimpleValueForKey:].cold.1
+ -[XCElementSnapshot _fetchSimpleValueForKey:].cold.2
+ -[XCElementSnapshot _fetchSimpleValueForKey:].cold.3
+ -[XCElementSnapshot copyWithZone:].cold.1
+ -[XCElementSnapshot indexPath].cold.1
+ -[XCElementSnapshot mergeTreeWithSnapshot:].cold.1
+ -[XCElementSnapshot replaceDescendant:withElement:].cold.1
+ -[XCTAccessibilityFramework _attributesForElement:iOSAttributes:error:].cold.1
+ -[XCTApplicationStateSnapshot initWithBundleID:path:runState:processID:activationPolicy:eventID:].cold.1
+ -[XCTAttachmentFutureMetadata initWithCoder:].cold.1
+ -[XCTAttachmentFutureMetadata initWithCoder:].cold.2
+ -[XCTAutomationSession detectRuntimeIssues].cold.1
+ -[XCTElementQuery _firstMatchingSnapshotForInput:transformers:relatedElements:noMatchesMessage:error:].cold.1
+ -[XCTElementQuery _snapshotForElement:error:].cold.2
+ -[XCTElementQuery initWithCoder:].cold.1
+ -[XCTElementQuery initWithRootElement:transformers:options:isMacOS:timeoutControls:].cold.1
+ -[XCTElementQueryTransformerPredicateValidator visitPredicateExpression:].cold.1
+ -[XCTElementQueryTransformerPredicateValidator visitPredicateExpression:].cold.2
+ -[XCTElementSnapshotRequest(PlatformImplementation) accessibilitySnapshotOrError:].cold.1
+ -[XCTElementSnapshotRequest(PlatformImplementation) safeParametersForParameters:].cold.1
+ -[XCTElementSortingTransformer initWithCoder:].cold.1
+ -[XCTImage initWithCGImage:metadata:orientation:].cold.1
+ -[XCTImage initWithData:encodedIn:metadata:].cold.1
+ -[XCTImage initWithData:encodedIn:metadata:].cold.2
+ -[XCTImage initWithData:encodedIn:metadata:].cold.3
+ -[XCTImage initWithData:encodedIn:metadata:].cold.4
+ -[XCTImage initWithImage:].cold.1
+ -[XCTImage initWithImage:].cold.2
+ -[XCTImage platformImage].cold.1
+ -[XCTLogArchiveRequest executeWithCompletion:].cold.1
+ -[XCTMainRunLoopIdleNotifier _queue_setUpRunLoopObserver].cold.1
+ -[XCTMainRunLoopIdleNotifier handleIdleObserved].cold.1
+ -[XCTSerializedTransportWrapper2 initWithCoder:].cold.1
+ XCAXAccessibilityAttributesForStringAttributes.cold.1
+ XCAXDefaultStringAttributes_iOS.cold.1
+ XCAXDefaultStringAttributes_macOS.cold.1
+ XCAXLocalizableStringsDataAttributes.cold.1
+ XCAXSnapshotAttributesForElementSnapshotKeys.cold.1
+ XCAXSnapshotAttributesForElementSnapshotKeys_iOS.cold.1
+ XCTASDefaultLog.cold.1
+ XCTAccessibilityFrameworkAssertThreadRequirement.cold.1
+ XCTClassesForAccessibilityAttributeDecoding.cold.1
+ XCTDefaultIdentifierFromSubrole.cold.1
+ XCTElementTypeFromRole.cold.1
+ XCTRuntimeIssueClasses.cold.1
+ XCTRuntimeIssueEncodingClasses.cold.1
+ XCUILargestRect.cold.1
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _XCTASFormatArraysAsMatrixWithRowPrefix.cold.1
+ _XCTASFormatArraysAsMatrixWithRowPrefix.cold.2
+ _XCTASLog.cold.1
+ _XCTClassNameToElementTypeMapping.cold.1
+ _XCUIFilterStringFromElementType.cold.1
+ __62-[XCTAutomationSession attributesForElement:attributes:reply:]_block_invoke.352
+ __66-[XCTAutomationSession initWithAccessibilityFramework:dataSource:]_block_invoke.245
+ __90-[XCTAutomationSession listenForRemoteConnectionViaSerializedTransportWrapper:completion:]_block_invoke.400
+ __90-[XCTAutomationSession listenForRemoteConnectionViaSerializedTransportWrapper:completion:]_block_invoke.404
+ __90-[XCTAutomationSession listenForRemoteConnectionViaSerializedTransportWrapper:completion:]_block_invoke.422
+ __OBJC_$_CLASS_METHODS_XCElementSnapshot(XCUITypeIdentification)
+ __XCSafeAttributeValue_block_invoke.67.cold.1
+ __XCUIFilterStringFromElementType
+ __XCUITypeStringFromElementType
+ __block_literal_global.1140
+ __block_literal_global.1202
+ __block_literal_global.554
+ _objc_msgSend$emptyImageWithSize:
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$stringByReplacingCharactersInRange:withString:
+ _xcToAXAuditTestMappings.cold.2
- __62-[XCTAutomationSession attributesForElement:attributes:reply:]_block_invoke.349
- __66-[XCTAutomationSession initWithAccessibilityFramework:dataSource:]_block_invoke.242
- __90-[XCTAutomationSession listenForRemoteConnectionViaSerializedTransportWrapper:completion:]_block_invoke.397
- __90-[XCTAutomationSession listenForRemoteConnectionViaSerializedTransportWrapper:completion:]_block_invoke.401
- __90-[XCTAutomationSession listenForRemoteConnectionViaSerializedTransportWrapper:completion:]_block_invoke.419
- __OBJC_$_CLASS_METHODS_XCElementSnapshot
- __OBJC_$_CLASS_PROP_LIST_XCElementSnapshot
- __block_literal_global.1122
- __block_literal_global.1184
- __block_literal_global.551
CStrings:
+ "'Any' does not correspond to a valid filter type and should never be passed to _XCUIFilterStringFromElementType()"
+ "Elements"
+ "Image data was nil. Using an empty image as a placeholder."
+ "XCUITypeIdentification"
+ "com.apple.dt.xctest.element-snapshot"
+ "es"
+ "lowercaseString"
+ "stringByReplacingCharactersInRange:withString:"
+ "utIdentifierString"

```
