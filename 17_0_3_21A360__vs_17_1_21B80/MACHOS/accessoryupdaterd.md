## accessoryupdaterd

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd`

```diff

-916.0.46.0.0
-  __TEXT.__text: 0x447cc
-  __TEXT.__auth_stubs: 0x1110
-  __TEXT.__objc_stubs: 0x73e0
-  __TEXT.__objc_methlist: 0x3070
+916.40.22.0.2
+  __TEXT.__text: 0x46d94
+  __TEXT.__auth_stubs: 0x1140
+  __TEXT.__objc_stubs: 0x7480
+  __TEXT.__objc_methlist: 0x3188
+  __TEXT.__cstring: 0xb7fd
+  __TEXT.__objc_methname: 0x88e6
+  __TEXT.__oslogstring: 0x42bd
+  __TEXT.__objc_classname: 0x685
+  __TEXT.__objc_methtype: 0x1ac7
   __TEXT.__const: 0x2c8
-  __TEXT.__objc_methname: 0x8805
-  __TEXT.__cstring: 0xb0cf
-  __TEXT.__oslogstring: 0x40b6
-  __TEXT.__objc_classname: 0x62f
-  __TEXT.__objc_methtype: 0x19fa
   __TEXT.__gcc_except_tab: 0x3e0
   __TEXT.__dlopen_cstrs: 0xf6
   __TEXT.__ustring: 0x12c
-  __TEXT.__unwind_info: 0x1018
-  __DATA_CONST.__auth_got: 0x898
-  __DATA_CONST.__got: 0x248
+  __TEXT.__unwind_info: 0x107c
+  __DATA_CONST.__auth_got: 0x8b0
+  __DATA_CONST.__got: 0x250
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1090
-  __DATA_CONST.__cfstring: 0x77c0
-  __DATA_CONST.__objc_classlist: 0x180
+  __DATA_CONST.__const: 0x1370
+  __DATA_CONST.__cfstring: 0x7fa0
+  __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0xb8
+  __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x97d8
-  __DATA.__objc_selrefs: 0x2188
-  __DATA.__objc_protorefs: 0x50
-  __DATA.__objc_classrefs: 0x2c8
-  __DATA.__objc_superrefs: 0x178
-  __DATA.__objc_ivar: 0x518
-  __DATA.__objc_data: 0xf00
-  __DATA.__data: 0xa43
+  __DATA.__objc_const: 0xa228
+  __DATA.__objc_selrefs: 0x21b8
+  __DATA.__objc_protorefs: 0x60
+  __DATA.__objc_classrefs: 0x2d8
+  __DATA.__objc_superrefs: 0x188
+  __DATA.__objc_ivar: 0x538
+  __DATA.__objc_data: 0xfa0
+  __DATA.__data: 0xb03
   __DATA.__bss: 0x478
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1B1FF7E2-1A1C-3775-B543-E7BFC65D6EF8
-  Functions: 1738
-  Symbols:   402
-  CStrings:  4498
+  UUID: A0E65ED3-D060-386D-9D12-B249F036D9EF
+  Functions: 1784
+  Symbols:   406
+  CStrings:  4665
 
Symbols:
+ _UARPFirmwareStagingCompletionStatusToString
+ _kUARPSupportedAccessoryCaseModelNameIdentifier
+ _objc_autoreleaseReturnValue
+ _objc_retain_x9
CStrings:
+ "\x02"
+ "\x05"
+ " (%@)"
+ "%s: Failed to create power assertion %@ with error %d"
+ "%s: Failed to release power assertion with error %d"
+ "%s: Invalid powerAssertionID received from caller"
+ "%s: _xpcConnection is nil"
+ "-[UARPManagerAUD addAccessory:assetID:]"
+ "-[UARPManagerAUD removeAccessory:]"
+ "-[UARPManagerAUD stagingCompleteForAccessoryID:assetID:status:]"
+ "-[UARPManagerListener stagingCompleteForAccessoryID:assetID:status:]"
+ "-[UARPObserverListener addAccessoryID:assetID:]"
+ "-[UARPObserverListener firmwareUpdateProgressForAccessoryID:assetID:bytesSent:bytesTotal:]"
+ "-[UARPObserverListener removeAccessoryID:]"
+ "-[UARPObserverListener stagingCompleteForAccessoryID:assetID:status:]"
+ "-[UARPObserverUpdate remoteObject]"
+ "-[UARPObserverUpdate remoteObject]_block_invoke"
+ "-[UARPObserverUpdate xpcConnectionToRequestor]"
+ "@\"NSXPCListenerEndpoint\""
+ "@\"UARPObserverListener\""
+ "AUDeveloperSettingsLocation"
+ "AUDeveloperSettingsLocation.plist"
+ "AUDeveloperSettingsOverride"
+ "AUObserverXPCClient"
+ "AUObserverXPCProvider"
+ "AUSettingsProgressActiveUpdate"
+ "AUSettingsProgressComplete"
+ "AUSettingsProgressKeyBuild"
+ "AUSettingsProgressKeyBytesSent"
+ "AUSettingsProgressKeyBytesTotal"
+ "About"
+ "Accessories Firmware Update"
+ "Active Version"
+ "Asset Location"
+ "Asset URL Override"
+ "BASEJUMPER"
+ "BOOL createPowerAssertion(NSString *, IOPMAssertionID *)"
+ "BOOL releasePowerAssertion(IOPMAssertionID)"
+ "Build"
+ "CUSTOMER"
+ "CUSTOMER_STAGING"
+ "CUSTOM_BASEJUMPER_BUILD"
+ "Could not create connection to UUID %@"
+ "Custom Basejumper Build"
+ "Custom Build"
+ "Custom Configuration"
+ "Custom Livability Train"
+ "Customer Staging"
+ "DawnB"
+ "Default Configuration"
+ "Details"
+ "Disable OTA Updates"
+ "Duplicate connection detected for UUID %@"
+ "Error getting supplemental asset location for accessory:%@"
+ "Failed to clean up SupplementalAsset %@ with error %@"
+ "Fusing"
+ "Hardware Revision"
+ "INTERNAL_SEED"
+ "Internal Development Firmware should only be installed on Apple Owned Units (AOU)"
+ "LATEST_BASEJUMPER"
+ "LIVABILITY"
+ "Model Number"
+ "No connection detected for UUID %@"
+ "PUBLIC_SEED"
+ "Perform Supplemental Asset query:%@"
+ "Pre-release Beta Program"
+ "RECEIVED %s: %@ %@ status=%s"
+ "SELECT_BASEJUMPER_LOCATION"
+ "SELECT_LOCATION"
+ "Serial Number"
+ "Supplemental Asset Location"
+ "Supplemental Asset remoteURL = %@"
+ "Supplemental Build"
+ "Supplemental Train"
+ "Train"
+ "UARPObserverListener"
+ "UARPObserverUpdate"
+ "[UARPManager stagingCompleteForAccessoryID:assetID:status:] must be overriden"
+ "_observerListener"
+ "_registeredObservers"
+ "_remoteEndpoint"
+ "addObserver:withEndpoint:"
+ "assetURL"
+ "checkmark"
+ "com.apple.AUDeveloperSettings.followup"
+ "com.apple.accessoryupdater.observer"
+ "customerOnly"
+ "id"
+ "initWithListenerEndpoint:"
+ "initWithRemoteServiceEndpoint:"
+ "items"
+ "kAUSettingsProgressActiveSerialNumber"
+ "label"
+ "observer"
+ "removeObserver:"
+ "stagingCompleteForAccessoryID:assetID:status:"
+ "supplementalAssetLocation"
+ "supplementalBasejumperBuild"
+ "supplementalBasejumperTrain"
+ "v24@0:8@\"NSUUID\"16"
+ "v24@0:8@\"UARPAccessoryID\"16"
+ "v32@0:8@\"NSUUID\"16@\"NSXPCListenerEndpoint\"24"
+ "v40@0:8@\"UARPAccessoryID\"16@\"UARPAssetID\"24Q32"
+ "v40@0:8@16@24Q32"
+ "xpcConnectionToRequestor"
- "Dawn"
- "Perform supplemental asset query:%@"
- "accessory.assetID.remoteURL = %@"

```
