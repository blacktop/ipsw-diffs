## EAUpdaterService

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/EAUpdaterService.xpc/EAUpdaterService`

```diff

-916.80.2.0.1
-  __TEXT.__text: 0xff64
+975.100.86.0.1
+  __TEXT.__text: 0x10550
   __TEXT.__auth_stubs: 0x5c0
-  __TEXT.__objc_stubs: 0x3120
+  __TEXT.__objc_stubs: 0x31e0
   __TEXT.__objc_methlist: 0xbe0
-  __TEXT.__cstring: 0x6873
+  __TEXT.__cstring: 0x6aae
   __TEXT.__const: 0x40
   __TEXT.__gcc_except_tab: 0x104
-  __TEXT.__objc_methname: 0x37b1
+  __TEXT.__objc_methname: 0x3853
   __TEXT.__oslogstring: 0x233
   __TEXT.__objc_classname: 0x107
   __TEXT.__objc_methtype: 0x794
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0x3a8
+  __TEXT.__unwind_info: 0x3cc
   __DATA_CONST.__auth_got: 0x2f0
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xdb8
-  __DATA_CONST.__cfstring: 0x5760
+  __DATA_CONST.__const: 0xf00
+  __DATA_CONST.__cfstring: 0x5b60
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x150
+  __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0x2328
-  __DATA.__objc_selrefs: 0xeb0
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x148
-  __DATA.__objc_superrefs: 0x38
+  __DATA.__objc_selrefs: 0xee0
   __DATA.__objc_ivar: 0x1ac
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x300
-  __DATA.__bss: 0x78
+  __DATA.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 341
-  Symbols:   548
-  CStrings:  1636
+  Functions: 349
+  Symbols:   587
+  CStrings:  1676
 
Symbols:
+ _OBJC_CLASS_$_UARPSupportedAccessory
+ _UARPStringPcapFilesFilepath
+ _dropboxFileUpdateForAccessoryID
+ _findPartnerSerialNumberForAccessory
+ _findPartnerSerialNumbersInDatabase
+ _getAccessoryDatabaseForAccessoryID
+ _isOTAUpdateDisabledForAccessoryID
+ _kDropboxVersionKey
+ _kFirmwareDirectoryName
+ _kReleaseNotesDirectoryName
+ _kUARPStringMetadataApplePersonalizationECIDData
+ _kUARPStringMetadataApplePersonalizationFTABPayloadDigestFilename
+ _kUARPStringMetadataApplePersonalizationLife
+ _kUARPStringMetadataApplePersonalizationManifestEpoch
+ _kUARPStringMetadataApplePersonalizationManifestSuffix
+ _kUARPStringMetadataApplePersonalizationPayloadDigestFilename
+ _kUARPStringMetadataApplePersonalizationProvisioning
+ _kUARPStringMetadataApplePersonalizedManifest
+ _kUARPStringMetadataComposePropertyListPayload
+ _kUARPStringMetadataComposeVersionBVERStringFile
+ _kUARPStringMetadataComposeVersionStringFile
+ _kUARPStringPcapFiles
+ _kUARPStringPersonalizationOptionLife
+ _kUARPStringPersonalizationOptionManifestEpoch
+ _kUARPStringPersonalizationOptionProvisioning
+ _kUARPStringTMAPAppleModelNumber
+ _kUARPStringTMAPEventFields
+ _kUARPStringTMAPEventIndex
+ _kUARPStringTMAPEventName
+ _kUARPStringTMAPEvents
+ _kUARPStringTMAPFieldLength
+ _kUARPStringTMAPFieldName
+ _kUARPStringTMAPFieldType
+ _kUARPStringTMAPTypeString
+ _kUARPStringTMAPTypeUnsignedInteger
+ _kUARPStringTMAPVersion
+ _kUARPSupportedAccessoryKeyDFUMode
+ _kUARPSupportedAccessoryKeyIsSimulator
+ _kUARPSupportedAccessoryKeySupportsFriendlyName
CStrings:
+ "DFUMode"
+ "DawnE"
+ "EventFields"
+ "EventIndex"
+ "EventName"
+ "Events"
+ "FieldLength"
+ "FieldName"
+ "FieldType"
+ "IsSimulator"
+ "Life"
+ "ManifestEpoch"
+ "Personalization ECID Data"
+ "Personalization FTAB Payload Digest Filename"
+ "Personalization Life"
+ "Personalization Manifest Epoch"
+ "Personalization Manifest Suffix"
+ "Personalization Payload Digest Filename"
+ "Personalization Provisioning"
+ "Personalized Manifest"
+ "Property List Payload"
+ "Provisioning"
+ "SupportsFriendlyName"
+ "T@\"NSString\",?,R,C"
+ "UnsignedInteger"
+ "Version"
+ "Version BVER File"
+ "Version File"
+ "dropboxVersion"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "findByAppleModelNumber:"
+ "firmware"
+ "hwFusingType"
+ "pathWithComponents:"
+ "pcapfiles"
+ "prod"
+ "releasenotes"
+ "supportsInternalSettings"
+ "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
- "DawnD"

```
