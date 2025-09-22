## InputAnalyticsServer

> `/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer`

```diff

-102.100.0.0.0
-  __TEXT.__text: 0x44a9c
+108.0.0.0.0
+  __TEXT.__text: 0x45544
   __TEXT.__auth_stubs: 0xc90
-  __TEXT.__objc_methlist: 0x3964
-  __TEXT.__const: 0x2f0
-  __TEXT.__cstring: 0x3389
-  __TEXT.__oslogstring: 0x4656
-  __TEXT.__gcc_except_tab: 0x684
+  __TEXT.__objc_methlist: 0x39bc
+  __TEXT.__const: 0x2e0
+  __TEXT.__cstring: 0x3649
+  __TEXT.__oslogstring: 0x46e6
+  __TEXT.__gcc_except_tab: 0x690
   __TEXT.__swift5_typeref: 0x10d
   __TEXT.__swift5_capture: 0x98
   __TEXT.__constg_swiftt: 0x4c

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0xce8
+  __TEXT.__unwind_info: 0xcf8
   __TEXT.__eh_frame: 0x310
-  __TEXT.__objc_classname: 0x816
-  __TEXT.__objc_methname: 0x898d
-  __TEXT.__objc_methtype: 0xbda
-  __TEXT.__objc_stubs: 0x6b00
-  __DATA_CONST.__got: 0xed0
-  __DATA_CONST.__const: 0xe60
-  __DATA_CONST.__objc_classlist: 0x230
+  __TEXT.__objc_classname: 0x834
+  __TEXT.__objc_methname: 0x8ac4
+  __TEXT.__objc_methtype: 0xc16
+  __TEXT.__objc_stubs: 0x6be0
+  __DATA_CONST.__got: 0xed8
+  __DATA_CONST.__const: 0xe80
+  __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1db0
+  __DATA_CONST.__objc_selrefs: 0x1de8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__auth_got: 0x658
   __AUTH_CONST.__const: 0xd38
-  __AUTH_CONST.__cfstring: 0x3840
-  __AUTH_CONST.__objc_const: 0x6610
+  __AUTH_CONST.__cfstring: 0x3ae0
+  __AUTH_CONST.__objc_const: 0x6740
   __AUTH_CONST.__objc_intobj: 0xcf0
   __AUTH_CONST.__objc_arrayobj: 0x120
-  __AUTH.__objc_data: 0x838
+  __AUTH.__objc_data: 0x888
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x4a8
+  __DATA.__objc_ivar: 0x4b4
   __DATA.__data: 0x3b0
   __DATA.__bss: 0x1b8
   __DATA_DIRTY.__objc_data: 0xde8

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B0948C84-B044-3B3F-9E51-CE8F9DDC8E4B
-  Functions: 1618
+  UUID: C1F9971B-D19A-3E65-950A-C4C799A6302F
+  Functions: 1625
   Symbols:   597
-  CStrings:  2917
+  CStrings:  2975
 
Symbols:
+ _IAPayloadKeyImageGenerationFeatureModel
- __swift_FORCE_LOAD_$_swiftCoreImage
CStrings:
+ "%@:%@"
+ "%@=[%@]"
+ "@\"<IASImageGenerationCreationAnalyzerTestDelegateProtocol>\""
+ "C\""
+ "Expected FeatureDetails in HandoffRequested"
+ "Expected FeatureDetails in payload"
+ "Expected HandoffModel in HandoffRequested"
+ "Expected slotsAndReponse to be a dictionary"
+ "Expected slotsAndReponses to be present"
+ "IASImageGenerationUtilities"
+ "Incorrect UI for PanelAppeared after PanelRequested"
+ "Incorrect UI for subsequent PanelAppeared"
+ "Invalid numFilesRemoved"
+ "Invalid numFilesRemoved for slot form"
+ "Invalid numImagesRemoved"
+ "Invalid numImagesRemoved for slot form"
+ "No prompt for OEA"
+ "No prompt nor system prompt present for Montara"
+ "Rewrite should have a signle result index"
+ "Rewrite/Compose should have numResultsOffered == 1"
+ "SlotID should be present iff isForSlotForm == true"
+ "T@\"<IASImageGenerationCreationAnalyzerTestDelegateProtocol>\",W,N,V_testDelegate"
+ "T@\"NSDictionary\",C,N,V_featureModel"
+ "TQ,N,V_engagementIndex"
+ "Unknown slot type"
+ "[%{private}@] handleResultsRequestedForMontaraAndOEA:isInitialRequest: payloads are malformed, Prompt should be present but it is not"
+ "[%{private}@] handleResultsRequestedForMontaraAndOEA:isInitialRequest: payloads are malformed, neither Prompt nor SystemPrompt is present"
+ "_engagementIndex"
+ "_testDelegate"
+ "didPublishBiomeEvent:"
+ "engagementIndex"
+ "formattedStringFromFeatureModel:"
+ "handleResultsRequestedSignal:isInitialRequest:"
+ "messages-background"
+ "reverseObjectEnumerator"
+ "setEngagementIndex:"
+ "setTestDelegate:"
+ "testDelegate"
- "3#"
- "[%{private}@] handleResultsRequestedForMontara:isRefinement: payloads are malformed, neither Prompt nor SystemPrompt is present"
- "handleResultsRequestedForMontara:isInitialRequest:"

```
