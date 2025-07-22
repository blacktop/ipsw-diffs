## uarpd

> `/usr/libexec/uarpd`

```diff

-1338.0.46.502.1
-  __TEXT.__text: 0x7f28c
-  __TEXT.__auth_stubs: 0x900
-  __TEXT.__objc_stubs: 0x7660
-  __TEXT.__objc_methlist: 0x65b0
-  __TEXT.__objc_methname: 0xad4f
-  __TEXT.__objc_classname: 0x1526
-  __TEXT.__objc_methtype: 0x258f
+1338.0.62.0.1
+  __TEXT.__text: 0x81a50
+  __TEXT.__auth_stubs: 0x920
+  __TEXT.__objc_stubs: 0x7800
+  __TEXT.__objc_methlist: 0x6728
+  __TEXT.__objc_methname: 0xb030
+  __TEXT.__objc_classname: 0x158e
+  __TEXT.__objc_methtype: 0x2599
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x7ceb
-  __TEXT.__oslogstring: 0x5739
-  __TEXT.__gcc_except_tab: 0x144
-  __TEXT.__unwind_info: 0x19c8
-  __DATA_CONST.__auth_got: 0x490
-  __DATA_CONST.__got: 0x460
-  __DATA_CONST.__const: 0xdc0
-  __DATA_CONST.__cfstring: 0x3b20
-  __DATA_CONST.__objc_classlist: 0x478
+  __TEXT.__cstring: 0x817b
+  __TEXT.__oslogstring: 0x5b19
+  __TEXT.__gcc_except_tab: 0x158
+  __TEXT.__unwind_info: 0x1a28
+  __DATA_CONST.__auth_got: 0x4a0
+  __DATA_CONST.__got: 0x470
+  __DATA_CONST.__const: 0xf40
+  __DATA_CONST.__cfstring: 0x41e0
+  __DATA_CONST.__objc_classlist: 0x490
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x460
+  __DATA_CONST.__objc_superrefs: 0x478
   __DATA_CONST.__objc_intobj: 0x3f0
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0xcbf0
-  __DATA.__objc_selrefs: 0x2420
-  __DATA.__objc_ivar: 0x8a4
-  __DATA.__objc_data: 0x2cb0
+  __DATA.__objc_const: 0xd018
+  __DATA.__objc_selrefs: 0x24b8
+  __DATA.__objc_ivar: 0x8e4
+  __DATA.__objc_data: 0x2da0
   __DATA.__data: 0x4f0
   __DATA.__bss: 0x11c0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/UARPAssetManager.framework/UARPAssetManager

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: 68AD73C4-3BDF-34A5-97C4-E7E4ABE4C9DB
-  Functions: 2997
-  Symbols:   201
-  CStrings:  4045
+  UUID: 0B1B624F-CBCC-3018-9E75-D01570B61070
+  Functions: 3036
+  Symbols:   203
+  CStrings:  4211
 
Symbols:
+ _IOPMAssertionCreateWithName
+ _IOPMAssertionRelease
CStrings:
+ "%@-%@-%@"
+ "%@.%@"
+ "%c%c"
+ "%lu-%lu-%lu"
+ "%s: Created power assertion for %@"
+ "%s: Failed to create power assertion for %@; error %d"
+ "%s: Failed to release power assertion for %@; error %d"
+ "%s: No power assertion to release for %@"
+ "%s: Outstanding Info Property %@ (%@)for endpoint component %@ "
+ "%s: Outstanding Info Property for endpoint configuration: %@ (%@)"
+ "%s: Outstanding Preflight Info Property %@ (%@) for endpoint component %@ "
+ "%s: Previous power assertion created for %@"
+ "%s: Query Bulk Info Property for endpoint configuration: %@ (%@)"
+ "%s: Query Info Properties for endpoint component %@ "
+ "%s: Released power assertion for %@"
+ "%s: Releasing power assertion for %@"
+ "%s: Responded Bulk Info Property %@ (%@) for endpoint configuration %@"
+ "%s: Responded Bulk Info Property for endpoint configuration: %@ (%@)"
+ "%s: Taking power assertion for %@"
+ "%s: Wait for Outstanding Info Properties for endpoint component %@ "
+ "%s: component %@ outstandingInfoProperties does not contain %@ (%@), ignoring"
+ "%s: host endpoint uuid was nil, saving %@"
+ "%s: outstandingInfoProperties does not contain %@ (%@), ignoring"
+ "%s: processDeploymentRules: failed to process"
+ "%s: processPersonalizationTickets: failed to process"
+ "-[UARPHostEndpoint powerAssertionCreate]"
+ "-[UARPHostEndpoint powerAssertionRelease]"
+ "2"
+ "<%@: %@ until %@>"
+ "<%@: %lu until %@>"
+ "@\"NSDate\""
+ "Apple Info Ap Board ID"
+ "Apple Info Ap Chip ID"
+ "Apple Info Ap Production Mode"
+ "Apple Info Ap Security Mode"
+ "Apple Info Apple Model Number"
+ "Apple Info Asset Identifer"
+ "Apple Info Board ID"
+ "Apple Info Chip Epoch"
+ "Apple Info Chip ID"
+ "Apple Info Chip Revision"
+ "Apple Info ECID"
+ "Apple Info ECID Data"
+ "Apple Info Enable Mix Match"
+ "Apple Info FTAB Generation"
+ "Apple Info HW Fusing Type"
+ "Apple Info Hardware Specific"
+ "Apple Info Logical Unit Number"
+ "Apple Info Manifest Prefix"
+ "Apple Info Nonce"
+ "Apple Info Personalization Life"
+ "Apple Info Personalization Manifest Epoch"
+ "Apple Info Personalization Manifest Suffix"
+ "Apple Info Personalization Nonce Hash"
+ "Apple Info Personalization Nonce Seed"
+ "Apple Info Personalization Provisioning"
+ "Apple Info Prefix Needs Logical Unit Number"
+ "Apple Info Production Mode"
+ "Apple Info Real Hdcp Key Present"
+ "Apple Info Requires Personalization"
+ "Apple Info Security Domain"
+ "Apple Info Security Mode"
+ "Apple Info SoC Live Nonce"
+ "Apple Info Suffix Needs Logical Unit Number"
+ "Apple Info Ticket Long Name"
+ "AppleModelNumbers"
+ "Country"
+ "Country Rules"
+ "Deployment Rule Country"
+ "Deployment Rule Percentage"
+ "Deployment Rules"
+ "Percentage Limit"
+ "Percentage Rules"
+ "PreventUserIdleSystemSleep"
+ "Single Apple Model Number or Multiple Apple Model Numbers must be provided"
+ "T@\"NSDate\",R,V_untilDate"
+ "T@\"NSMutableArray\",C,V_preflightInfoProperties"
+ "T@\"NSString\",R,V_countryCode"
+ "TMAP Apple Model Number must be String and not nil."
+ "TMAP Apple Model Numbers must be Array and not nil."
+ "TQ,R,V_percentageLimit"
+ "UARPDeploymentRules"
+ "UARPMetaDataHostDeploymentRuleCountry"
+ "UARPMetaDataHostDeploymentRulePercentage"
+ "Until Day"
+ "Until Month"
+ "Until Year"
+ "_appleModelNumbers"
+ "_completedAssets"
+ "_countryRules"
+ "_percentageLimit"
+ "_percentageRules"
+ "_powerAssertionID"
+ "_powerAssertionName"
+ "_preflightInfoProperties"
+ "_untilDate"
+ "_untilDay"
+ "_untilMonth"
+ "_untilYear"
+ "allObjects"
+ "com.apple.uarp.uarpd.powerassertion"
+ "countryRules"
+ "dateFromString:"
+ "initWithEvents:appleModelNumbers:endian:"
+ "initWithEvents:endian:"
+ "initWithObjects:"
+ "initWithProjectSourceVersion:projectBuildVersion:"
+ "initWithRulesDictionary:"
+ "percentageLimit"
+ "percentageRules"
+ "powerAssertionCreate"
+ "powerAssertionRelease"
+ "preflightInfoProperties"
+ "processCountryDeploymentRules:"
+ "processDeploymentRules:"
+ "processPercentageDeploymentRules:"
+ "setPreflightInfoProperties:"
+ "tlvNameForAppleProperty:"
+ "tlvNameForType:"
+ "untilDate"
+ "yyyy-MM-dd"
- "%s: Outstanding Info Properties for endpoint component %@"
- "%s: Outstanding Info Properties for endpoint configuration %@"
- "%s: component %@ outstandingInfoProperties does not contain 0x%08x, ignoring"
- "%s: outstandingInfoProperties does not contain 0x%08x, ignoring"
- "%s: processPersonalizationTickets: failed to process personalization tickets"
- "-[UARPEndpointLayer3 notifyAssetFullyStaged:processingStatus:]"
- "-[UARPHostManager layer3EndpointAssetFullyStaged:asset:processingStatus:]"
- "-[UARPHostManager layer3EndpointAssetFullyStaged:asset:processingStatus:]_block_invoke"
- "notifyAssetFullyStaged:processingStatus:"

```
