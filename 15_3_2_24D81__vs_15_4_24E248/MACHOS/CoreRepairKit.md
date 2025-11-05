## CoreRepairKit

> `/System/Library/Templates/Data/Library/Frameworks/CoreRepairKit.framework/Versions/A/CoreRepairKit`

```diff

-645.80.16.0.0
-  __TEXT.__text: 0x5c68
-  __TEXT.__auth_stubs: 0x2a0
-  __TEXT.__objc_stubs: 0x820
-  __TEXT.__objc_methlist: 0x19c
-  __TEXT.__const: 0x3c8
-  __TEXT.__cstring: 0x3c9
-  __TEXT.__oslogstring: 0x6b4
-  __TEXT.__objc_classname: 0x1b
-  __TEXT.__objc_methname: 0x6ec
-  __TEXT.__objc_methtype: 0xdb
-  __TEXT.__unwind_info: 0x120
-  __DATA_CONST.__auth_got: 0x158
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__const: 0x20
-  __DATA_CONST.__cfstring: 0x580
-  __DATA_CONST.__objc_classlist: 0x10
+696.100.57.0.0
+  __TEXT.__text: 0x814
+  __TEXT.__auth_stubs: 0xd0
+  __TEXT.__objc_stubs: 0x220
+  __TEXT.__objc_methlist: 0xbc
+  __TEXT.__const: 0x58
+  __TEXT.__cstring: 0x2a
+  __TEXT.__oslogstring: 0xf1
+  __TEXT.__objc_classname: 0xf
+  __TEXT.__objc_methname: 0x280
+  __TEXT.__objc_methtype: 0x32
+  __TEXT.__unwind_info: 0x80
+  __DATA_CONST.__auth_got: 0x70
+  __DATA_CONST.__got: 0x30
+  __DATA_CONST.__cfstring: 0x80
+  __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_arraydata: 0x28
-  __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x120
-  __DATA.__objc_selrefs: 0x278
-  __DATA.__objc_data: 0xa0
-  __DATA.__bss: 0x10
+  __DATA.__objc_const: 0x90
+  __DATA.__objc_selrefs: 0xd0
+  __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
   - @rpath/CoreRepairCore.framework/Versions/A/CoreRepairCore
-  UUID: 8E4510D4-C34E-3F77-82EF-31989EFBBCD8
-  Functions: 110
-  Symbols:   82
-  CStrings:  239
+  UUID: F3CAF747-A8F5-3A22-90CE-0223AC5648EB
+  Functions: 23
+  Symbols:   31
+  CStrings:  45
 
Symbols:
+ _OBJC_CLASS_$_CRFDRUtils
- _AMFDRCreateTypeWithOptions
- _AMFDRCreateWithOptions
- _AMFDRDataCopyManifest
- _AMFDRDataCopySealingManifestProperty
- _AMFDRSealingManifestCopyDataClassesInstancesAndProperties
- _AMFDRSealingManifestCopyInstanceForClass
- _AMFDRSealingManifestCopyLocalDataForClass
- _AMFDRSealingManifestCopyMultiInstanceForClass
- _AMFDRSealingMapCopyDataClassesAndInstancesWithAttribute
- _AMFDRSealingMapCopyDataClassesWithAttribute
- _AMFDRSealingMapCopyLocalData
- _AMFDRSealingMapCopyManifestProperties
- _AMFDRSealingMapCopyMultiInstanceForClass
- _AMFDRSealingMapCopyPropertyWithTag
- _AMFDRSealingMapPopulateSealingManifest
- _AMFDRSetOption
- _AMSupportSafeRelease
- _CFDictionaryCreateMutable
- _CFDictionarySetValue
- _CRErrorDomain
- _NSLocalizedDescriptionKey
- _OBJC_CLASS_$_CREANController
- _OBJC_CLASS_$_NSArray
- _OBJC_CLASS_$_NSConstantArray
- _OBJC_CLASS_$_NSDictionary
- _OBJC_CLASS_$_NSError
- _OBJC_CLASS_$_NSMutableArray
- _OBJC_CLASS_$_NSMutableDictionary
- _OBJC_CLASS_$_NSMutableSet
- _OBJC_CLASS_$_NSPredicate
- _OBJC_CLASS_$_NSRegularExpression
- _OBJC_CLASS_$_NSSet
- _OBJC_CLASS_$_NSString
- _OBJC_CLASS_$_NSValue
- __NSConcreteStackBlock
- ___kCFBooleanTrue
- _bzero
- _dispatch_once
- _kAMFDRSealingMapAttributeRequiredToSeal
- _kCFAllocatorDefault
- _kCFBooleanFalse
- _kCFBooleanTrue
- _kCFTypeDictionaryKeyCallBacks
- _kCFTypeDictionaryValueCallBacks
- _objc_alloc
- _objc_alloc_init
- _objc_autorelease
- _objc_enumerationMutation
- _objc_opt_class
- _objc_opt_isKindOfClass
- _objc_opt_new
- _objc_retainAutorelease
CStrings:
+ "isCoverGlassRepaired"
+ "isVolumeButtonRepaired"
- "%@"
- "([a-zA-Z0-9#]{4})-(.*$)"
- "1"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@48@0:8{?=**}16Q32@40"
- "AllowIncompleteData"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B28@0:8B16^@20"
- "B28@0:8i16^@20"
- "B32@0:8@16^@24"
- "B40@0:8@16@24^@32"
- "CRFDRUtils"
- "Cannot copy %@ data from device"
- "Cannot copy %@ manifest from device"
- "Cannot copy sealing manifest from device"
- "Classes is not an array"
- "Component %d is not supported for authorized repair for this device"
- "Copy manifest data failed, error = %@"
- "Data class is nil"
- "DataInstances and Classes count mismatch"
- "DataStore"
- "FDR-CA\\d{1,4}-ROOT-DC.*"
- "FDR-SS-DC.*"
- "FSCl"
- "Failed to create amfdr"
- "Failed to create fdrLocal"
- "Failed to create property value string"
- "Failed to decode sealing manifest: %@"
- "Failed to decode sealing map: %@"
- "Failed to get 'SrvT' property"
- "Failed to get DataInstance:%@"
- "Failed to get local manifest properties, error: %@"
- "Failed to get local sealing manifest"
- "Failed to get payload; stat: %d"
- "Failed to parse cert as img4; stat: %d"
- "Failed to parse cert chain; stat: %d"
- "Failed to parse cert common name from cert chain"
- "Failed to parse node in cert chain data = %@"
- "Failed to read EAN"
- "Failed to read live instances of %@: %@"
- "Failed to read live property of %@: %@"
- "Failed to read live sensor number, error: %@"
- "Failed to read local %@ data; error: %@"
- "Failed to read seal data"
- "Failed to read sealed instances of %@: %@"
- "Failed to read sealed property of %@: %@"
- "Failed to verify local %@ data; error: %@"
- "Getting local sealing manifest"
- "Live classes: %lu. Live instances: %lu"
- "Live property missing for %@: %@"
- "Local"
- "Local Sealing manifest fetch failed"
- "Local Sealing manifest fetch sucessful"
- "Local sealing manifest populate failed, error = %@"
- "MSRk"
- "MesaProvisionState"
- "MesaSensorIDSensorSN"
- "Missing live data: %@"
- "No EAN support."
- "Number of data classes and instances mismatches"
- "Number of live data classes and instances mismatches"
- "NvMR"
- "Parsed the following common names from cert in %@: %@"
- "Parsed the following common names from cert in seal: %@"
- "Property %@ does not exist"
- "ProvisionedLockedUnknownKey"
- "ProvisionedUnknownKey"
- "Query staged state failed"
- "QueryPath"
- "QueryPath_Straight"
- "RCSn"
- "Read live data: %d"
- "Read live data: %d. %@"
- "SELF MATCHES %@"
- "SealingManifest"
- "Skip reading unknown Mesa: %d"
- "SkipRecoverDataClasses"
- "SrvP"
- "SrvT"
- "SrvT: %@"
- "Unsealed %@: %@"
- "Unsealed: %@"
- "VerifyData"
- "^{__AMFDR=}16@0:8"
- "_createFDRLocal"
- "_getDataClassesFromSealingManifest"
- "_getDataClassesFromSealingMap"
- "_getManifestForDataClass:"
- "addObject:"
- "addObjectsFromArray:"
- "allObjects"
- "array"
- "arrayWithObjects:count:"
- "bytes"
- "containsObject:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "drp#"
- "errorWithDomain:code:userInfo:"
- "extractComponentsAndIdentifiers:"
- "filteredArrayUsingPredicate:"
- "findUnsealedDataWithError:"
- "findUnsealedDataWithKey:error:"
- "firstMatchInString:options:range:"
- "fixUpPseudoMSRk:mesaWithSCKey:"
- "getData:instance:"
- "getDataPayload:instance:"
- "getStringFromCert:WithTag:AndOID:"
- "getValue:"
- "hop0"
- "initWithBytes:length:"
- "initWithData:encoding:"
- "initWithPattern:options:error:"
- "isDataClassSupported:"
- "isEANSupported"
- "isEqualToString:"
- "length"
- "localManifestProperties"
- "localizedDescription"
- "mesa unpaired"
- "mesa unsealed"
- "minusSet:"
- "mutableCopy"
- "number of ranges:%ld"
- "numberOfRanges"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "predicateWithFormat:"
- "queryDeviceStagedSealedFromEAN:error:"
- "rangeAtIndex:"
- "readFDRDataFromEANWithDataClass:outData:stripPadding:"
- "removeObjectAtIndex:"
- "seal"
- "set"
- "setByAddingObject:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setWithArray:"
- "stringWithFormat:"
- "substringWithRange:"
- "v28@0:8@16B24"
- "v8@?0"
- "valueWithBytes:objCType:"
- "{?=Q{?=*Q}}"

```
