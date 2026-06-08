## LighthouseCoreMLModelStore

> `/System/Library/PrivateFrameworks/LighthouseCoreMLModelStore.framework/LighthouseCoreMLModelStore`

```diff

 3.0.0.0.0
-  __TEXT.__text: 0x2b90
-  __TEXT.__auth_stubs: 0x2f0
+  __TEXT.__text: 0x2838
   __TEXT.__objc_methlist: 0x2f0
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x173
+  __TEXT.__cstring: 0x179
   __TEXT.__oslogstring: 0x24a
-  __TEXT.__unwind_info: 0xf0
-  __TEXT.__objc_classname: 0x75
-  __TEXT.__objc_methname: 0x9cb
-  __TEXT.__objc_methtype: 0xd9
-  __TEXT.__objc_stubs: 0x840
-  __DATA_CONST.__got: 0x88
+  __TEXT.__unwind_info: 0xf8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x30
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x310
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x180
+  __DATA_CONST.__got: 0x88
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x200
   __AUTH_CONST.__objc_const: 0x600
   __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x40
   __DATA.__data: 0x18

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6A5CC514-F25F-3757-9AD0-7616273C7CC8
-  Functions: 85
-  Symbols:   370
-  CStrings:  206
+  UUID: 3B470761-DA18-34DD-80FE-48C5B5BE0D1E
+  Functions: 82
+  Symbols:   359
+  CStrings:  56
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x8
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _objc_release_x28
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x26
- _objc_retain_x27
- _objc_retain_x28
CStrings:
- ".cxx_destruct"
- "@\"LCFModelStoreModelMetadataProvider\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSString\""
- "@\"NSURL\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "@40@0:8@16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "B40@0:8@16@24@32"
- "LCFModelMetadata"
- "LCFModelStore"
- "LCFModelStoreModelMetadataProvider"
- "LCFModelStoreUserDefaults"
- "LCFModelStoreUtils"
- "SwitchToMobile"
- "T@\"LCFModelStoreModelMetadataProvider\",R,N,V_modelMetadataProvider"
- "T@\"NSDate\",C,N,V_dateCreated"
- "T@\"NSDate\",C,N,V_dateTrained"
- "T@\"NSDictionary\",C,N,V_custom"
- "T@\"NSString\",C,N,V_sha256"
- "T@\"NSString\",R,N,V_key"
- "T@\"NSURL\",R,N,V_emptyModelURL"
- "T@\"NSURL\",R,N,V_metadataPlistFileURL"
- "T@\"NSURL\",R,N,V_modelStoreRootURL"
- "T@\"NSURL\",R,N,V_modelStoreRootWithKeyURL"
- "T@\"NSURL\",R,N,V_originalEmptyModelURL"
- "TB,N,V_isAvailable"
- "TB,N,V_isImported"
- "TB,N,V_isLocal"
- "TB,N,V_isOriginalEmptyModel"
- "URLByAppendingPathComponent:"
- "URLByAppendingPathExtension:"
- "URLByDeletingPathExtension"
- "_custom"
- "_dateCreated"
- "_dateTrained"
- "_emptyModelURL"
- "_isAvailable"
- "_isImported"
- "_isLocal"
- "_isOriginalEmptyModel"
- "_key"
- "_metadataPlistFileURL"
- "_modelMetadataProvider"
- "_modelStoreRootURL"
- "_modelStoreRootWithKeyURL"
- "_originalEmptyModelURL"
- "_sha256"
- "addObject:"
- "allKeys"
- "appendData:"
- "appendFormat:"
- "bytes"
- "checkResourceIsReachableAndReturnError:"
- "clear"
- "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
- "copyItemAtURL:toURL:error:"
- "countByEnumeratingWithState:objects:count:"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "dataWithContentsOfURL:"
- "defaultManager"
- "deleteModel:"
- "emptyModelURL"
- "encodeWithCoder:"
- "encodedData"
- "fileExistsAtPath:"
- "finishEncoding"
- "getBaseLocalPath"
- "getBaseModelURL:modelConfig:"
- "getMetadata"
- "getModelConfig:"
- "getModelMetadata:"
- "getModelURL:"
- "init"
- "init:"
- "init:modelStoreRootURL:"
- "init:modelStoreRootURL:originalEmptyModelURL:"
- "initForReadingFromData:error:"
- "initRequiringSecureCoding:"
- "initWithCoder:"
- "initWithContentsOfURL:"
- "initWithDictionary:"
- "initWithSuiteName:"
- "isEnabledOnMacOS"
- "isEqual:"
- "isEqualToString:"
- "isPlatformMacOS"
- "isPlatformWatchOS"
- "isPlatformiOS"
- "isPlatformtvOS"
- "isSupportedPlatform"
- "key"
- "lastPathComponent"
- "lastTrainedDate"
- "length"
- "listModelNames"
- "markModelTrained:"
- "metadataPlistFileURL"
- "modelMetadataProvider"
- "modelStoreRootURL"
- "modelStoreRootWithKeyURL"
- "now"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "originalEmptyModelURL"
- "path"
- "removeItemAtURL:error:"
- "removeModelMetadata:"
- "setCustom:"
- "setDateCreated:"
- "setDateTrained:"
- "setIsAvailable:"
- "setIsImported:"
- "setIsLocal:"
- "setIsOriginalEmptyModel:"
- "setLastTrainedDate:"
- "setModelMetadata:key:value:"
- "setModelMetadata:metadata:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setSha256:"
- "setValue:forKey:"
- "sha256For:"
- "sha256ForURL:"
- "storeModel:"
- "storeModel:modelConfig:"
- "stringByAppendingString:"
- "stringWithCapacity:"
- "stringWithUTF8String:"
- "toDictionary"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "valueForKey:"
- "writeToURL:atomically:"
- "writeToURL:error:"

```
