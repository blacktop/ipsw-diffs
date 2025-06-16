## inboxupdaterd

> `/usr/libexec/inboxupdaterd`

```diff

-63.120.35.0.0
-  __TEXT.__text: 0x68014
-  __TEXT.__auth_stubs: 0x1170
-  __TEXT.__objc_stubs: 0x6400
-  __TEXT.__objc_methlist: 0x3084
-  __TEXT.__cstring: 0x3708
-  __TEXT.__objc_methname: 0x666b
-  __TEXT.__objc_classname: 0x4f6
+63.140.18.0.0
+  __TEXT.__text: 0x69638
+  __TEXT.__auth_stubs: 0x11b0
+  __TEXT.__objc_stubs: 0x6640
+  __TEXT.__objc_methlist: 0x30ec
+  __TEXT.__cstring: 0x3805
+  __TEXT.__objc_methname: 0x67fb
+  __TEXT.__objc_classname: 0x4fa
   __TEXT.__objc_methtype: 0x1232
   __TEXT.__const: 0x2a81
-  __TEXT.__oslogstring: 0x62b0
+  __TEXT.__oslogstring: 0x64f7
   __TEXT.__gcc_except_tab: 0x1548
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x16b0
-  __DATA_CONST.__auth_got: 0x8c8
+  __TEXT.__unwind_info: 0x16d8
+  __DATA_CONST.__auth_got: 0x8e8
   __DATA_CONST.__got: 0x338
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x9548
-  __DATA_CONST.__cfstring: 0x3100
+  __DATA_CONST.__const: 0x96d0
+  __DATA_CONST.__cfstring: 0x3280
   __DATA_CONST.__objc_classlist: 0x130
-  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8

   __DATA_CONST.__objc_arraydata: 0x4e8
   __DATA_CONST.__objc_arrayobj: 0x540
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x7950
-  __DATA.__objc_selrefs: 0x1d10
+  __DATA.__objc_const: 0x79a8
+  __DATA.__objc_selrefs: 0x1da8
   __DATA.__objc_ivar: 0x324
   __DATA.__objc_data: 0xbe0
   __DATA.__data: 0x1b00

   - /usr/lib/libamsupport.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8B998A28-7C24-3519-89C3-083ABDD8A281
-  Functions: 2925
-  Symbols:   391
-  CStrings:  3111
+  UUID: FB9D5AF2-E889-3C7D-BEBE-04C96CDEAAE5
+  Functions: 2960
+  Symbols:   395
+  CStrings:  3166
 
Symbols:
+ _CC_SHA1_Final
+ _CC_SHA1_Init
+ _CC_SHA1_Update
+ _arc4random_uniform
CStrings:
+ "An error happened while downloading update asset"
+ "An error happened while extracting update asset"
+ "An error happened while setting up asset file"
+ "Cannot read data from %{public}@ - %{public}@."
+ "Cannot read file %{public}@"
+ "Connection retry finished with error: %{public}@, total retry count: %lu"
+ "CurrentBuildVersion"
+ "Disassociating with WiFi..."
+ "EnterLPMAfterUpdateComplete"
+ "Failed receiving asset over multicast: %{public}@"
+ "Failed to compute asset file hash"
+ "Failed to connect to wifi with error %{public}@, waiting for %us"
+ "Failed to put device to low power mode, will shutdown instead (no longer wakeable)."
+ "IOPMUBootReasonLPMSU"
+ "Not able to find AppleDialogSPMIPMU. IOServiceGetMatchingServices returned 0x%x"
+ "Not able to get property value of IOPMUBootReasonLPMSU. IORegistryEntryGetProperty returned 0x%x"
+ "Not able to get property value of IOPMUPrimary. IORegistryEntryGetProperty returned 0x%x"
+ "Operation is successful."
+ "Putting device to low power mode per configuration."
+ "SHA-1"
+ "SSUNanSubscriberDiscoveredResult"
+ "SSUWiFiInfraConnFailed"
+ "SSUWiFiInfraConnSucceeded"
+ "Shutting down device (no longer wakeable)."
+ "StandbyIdleTimeout"
+ "Subscriber"
+ "TQ,N,V_globalRetryCount"
+ "WiFiConnectRetryTotalCount"
+ "_Measurement"
+ "_MeasurementAlgorithm"
+ "_assetRelativePathFromCatalog:assetPath:"
+ "_globalRetryCount"
+ "absoluteString"
+ "closeFile"
+ "directoryHash"
+ "disassociate"
+ "disassociateWithReason:"
+ "enterLPMAfterUpdateComplete"
+ "fileDescriptor"
+ "fileHandleForReadingAtPath:"
+ "fileHash"
+ "globalRetryCount"
+ "isFileURL"
+ "path"
+ "pathComponents"
+ "readDataUpToLength:error:"
+ "setGlobalRetryCount:"
+ "standbyIdleTimeout"
+ "stringByAppendingPathExtension:"
+ "stringByRemovingPercentEncoding"
+ "wakedUpFromLPM"
+ "xml"
- "Connection retry finished with error: %{public}@"
- "Failed receiving asset over multicast"
- "Failed to download update asset"
- "Failed to extract update asset"
- "Failed to put device to low power mode."
- "Failed to setup asset file"
- "IORegistryEntryGetProperty returned %d"
- "IOServiceGetMatchingServices returned %d"
- "Operation is succesful. Putting device to low power mode."
- "_assetRelativePathFromCatalog:"

```
