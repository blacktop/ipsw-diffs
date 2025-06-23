## inboxupdaterd

> `/usr/libexec/inboxupdaterd`

```diff

-132.0.0.0.0
-  __TEXT.__text: 0x69324
-  __TEXT.__auth_stubs: 0x11c0
-  __TEXT.__objc_stubs: 0x6480
-  __TEXT.__objc_methlist: 0x30a4
-  __TEXT.__cstring: 0x37a8
-  __TEXT.__objc_methname: 0x66e0
-  __TEXT.__objc_classname: 0x4f6
+144.0.0.0.0
+  __TEXT.__text: 0x6a828
+  __TEXT.__auth_stubs: 0x11e0
+  __TEXT.__objc_stubs: 0x6620
+  __TEXT.__objc_methlist: 0x30f4
+  __TEXT.__cstring: 0x37ff
+  __TEXT.__objc_methname: 0x67f3
+  __TEXT.__objc_classname: 0x4fa
   __TEXT.__objc_methtype: 0x1232
   __TEXT.__const: 0x6e70
-  __TEXT.__oslogstring: 0x635a
-  __TEXT.__gcc_except_tab: 0x1548
+  __TEXT.__oslogstring: 0x65f3
+  __TEXT.__gcc_except_tab: 0x155c
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x16f0
-  __DATA_CONST.__auth_got: 0x8f0
-  __DATA_CONST.__got: 0x338
+  __TEXT.__unwind_info: 0x1708
+  __DATA_CONST.__auth_got: 0x900
+  __DATA_CONST.__got: 0x330
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0xb568
-  __DATA_CONST.__cfstring: 0x31c0
+  __DATA_CONST.__const: 0xb718
+  __DATA_CONST.__cfstring: 0x3240
   __DATA_CONST.__objc_classlist: 0x130
-  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8

   __DATA_CONST.__objc_arraydata: 0x4e8
   __DATA_CONST.__objc_arrayobj: 0x540
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x7980
-  __DATA.__objc_selrefs: 0x1d30
-  __DATA.__objc_ivar: 0x328
+  __DATA.__objc_const: 0x79b0
+  __DATA.__objc_selrefs: 0x1da8
+  __DATA.__objc_ivar: 0x324
   __DATA.__objc_data: 0xbe0
   __DATA.__data: 0x1ba8
   __DATA.__bss: 0x110

   - /usr/lib/libamsupport.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0ECAFFD9-A143-3EA3-99FC-EA33187F56BD
-  Functions: 2946
-  Symbols:   396
-  CStrings:  3130
+  UUID: 8CA49615-A2E1-369B-B74A-45FB19C2CE5C
+  Functions: 2977
+  Symbols:   397
+  CStrings:  3166
 
Symbols:
+ _CC_SHA1_Final
+ _CC_SHA1_Init
+ _CC_SHA1_Update
- _CFPreferencesSetValue
- _kCFPreferencesCurrentUser
CStrings:
+ "/.exclave"
+ "An error happened while spinning loopback server"
+ "Bluetooth connection already established: %{public}@, ignore this new connection"
+ "Cannot read data from %{public}@ - %{public}@."
+ "Cannot read file %{public}@"
+ "Device is already secure BT connected"
+ "EnterLPMAfterUpdateComplete"
+ "Failed receiving asset over multicast: %{public}@"
+ "Failed to compute asset file hash"
+ "Failed to derive Device IDs for BT advertisement: %{public}@"
+ "Failed to derive Device IDs for BT connection: %{public}@"
+ "Failed to put device to low power mode, will shutdown instead (no longer wakeable)."
+ "IOPMUBootReasonLPMSU"
+ "IORegistryEntryGetProperty completed successfully!"
+ "IORegistryEntryGetProperty returned 0x%x when trying to get property value of IOPMUPrimary for current pmu entry."
+ "Not able to find AppleDialogSPMIPMU. IOServiceGetMatchingServices returned 0x%x"
+ "Not able to find primary pmu."
+ "Not able to get property value of IOPMUBootReasonLPMSU. IORegistryEntryGetProperty returned 0x%x"
+ "Operation is successful."
+ "Putting device to low power mode per configuration."
+ "SHA-1"
+ "Shutting down device (no longer wakeable)."
+ "StandbyIdleTimeout"
+ "Using device serial number %{public}@ as adv key"
+ "Using device serial number %{public}@ as link encryption key"
+ "_Measurement"
+ "_MeasurementAlgorithm"
+ "_assetRelativePathFromCatalog:assetPath:"
+ "absoluteString"
+ "closeFile"
+ "directoryHash"
+ "enterLPMAfterUpdateComplete"
+ "fileDescriptor"
+ "fileHandleForReadingAtPath:"
+ "fileHash"
+ "isFileURL"
+ "path"
+ "pathComponents"
+ "readDataUpToLength:error:"
+ "standbyIdleTimeout"
+ "stringByAppendingPathExtension:"
+ "stringByRemovingPercentEncoding"
+ "supportsSeaShip"
+ "wakedUpFromLPM"
+ "xml"
- "DownloadServerBaseURLOverride"
- "Failed receiving asset over multicast"
- "Failed to dervie Device IDs for BT advertisement: %{public}@"
- "Failed to dervie Device IDs for BT connection: %{public}@"
- "Failed to put device to low power mode."
- "IORegistryEntryGetProperty returned %d"
- "IOServiceGetMatchingServices returned %d"
- "Operation is succesful. Putting device to low power mode."
- "Setting Mobile Asset Base URL Override..."
- "Using device serial number %{public}@ as device key"
- "_assetRelativePathFromCatalog:"
- "_overrideSUAssetBaseURL"
- "com.apple.MobileAsset"
- "http://localhost:8080"

```
