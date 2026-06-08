## HIDDisplay

> `/System/Library/PrivateFrameworks/HIDDisplay.framework/HIDDisplay`

```diff

-2238.120.5.0.0
-  __TEXT.__text: 0x6fe8
-  __TEXT.__auth_stubs: 0x350
+2353.0.0.0.1
+  __TEXT.__text: 0x6664
   __TEXT.__objc_methlist: 0x37c
   __TEXT.__const: 0xe8
-  __TEXT.__cstring: 0x2b6
+  __TEXT.__cstring: 0x2be
   __TEXT.__oslogstring: 0xad0
-  __TEXT.__gcc_except_tab: 0x158
-  __TEXT.__unwind_info: 0x220
-  __TEXT.__objc_classname: 0xb0
-  __TEXT.__objc_methname: 0x6cd
-  __TEXT.__objc_methtype: 0x15d
-  __TEXT.__objc_stubs: 0xa20
-  __DATA_CONST.__got: 0xc0
+  __TEXT.__gcc_except_tab: 0xe8
+  __TEXT.__unwind_info: 0x218
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2c0
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x130
-  __AUTH_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__got: 0xc0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x3a0
   __AUTH_CONST.__objc_const: 0x5d0
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_dictobj: 0x208
   __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x34
   __DATA.__data: 0x58

   - /System/Library/PrivateFrameworks/HID.framework/HID
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 35E335F0-0732-35CC-A06E-1DECFF5F6A4A
-  Functions: 169
-  Symbols:   595
-  CStrings:  267
+  UUID: 2E3870E9-9020-3814-9C4C-F1C2358E50BD
+  Functions: 163
+  Symbols:   582
+  CStrings:  130
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- GCC_except_table18
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _objc_retain_x28
CStrings:
- ".cxx_destruct"
- "@\"HIDDevice\""
- "@\"HIDDisplayPresetInterface\""
- "@\"HIDManager\""
- "@\"NSArray\""
- "@\"NSDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@16@0:8"
- "@20@0:8I16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@24@0:8q16"
- "@32@0:8@16q24"
- "@?"
- "B16@0:8"
- "B24@0:8^@16"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B32@0:8^Q16^@24"
- "B32@0:8q16^@24"
- "B36@0:8C16Q20^@28"
- "HIDDisplayDeviceManagementInterface"
- "HIDDisplayIOReportingInterface"
- "HIDDisplayInterface"
- "HIDDisplayPresetData"
- "HIDDisplayPresetInterface"
- "HIDDisplayUserAdjustmentInterface"
- "Q"
- "Q16@0:8"
- "T@\"NSArray\",R"
- "T@\"NSArray\",R,V_presets"
- "T@\"NSData\",R"
- "T@\"NSString\",R,V_containerID"
- "TB,R"
- "TQ,R,V_registryID"
- "_containerID"
- "_dataHandler"
- "_deviceRef"
- "_index"
- "_manager"
- "_presets"
- "_queue"
- "_registryID"
- "_usageElementMap"
- "activate"
- "addObject:"
- "arrayWithObjects:count:"
- "bytes"
- "cancel"
- "capabilities"
- "close"
- "commit:error:"
- "commitElements:direction:error:"
- "containerID"
- "containsString:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createPresets"
- "dataUsingEncoding:"
- "dataValue"
- "dealloc"
- "description"
- "device"
- "devices"
- "dictionaryWithObjects:forKeys:count:"
- "elementsMatching:"
- "enumerateKeysAndObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "extract:error:"
- "extractContainerIDFromService:"
- "factoryReset:securityToken:error:"
- "get:"
- "getActivePresetIndex:"
- "getCurrentPresetIndex:"
- "getDeviceElements:"
- "getFactoryDefaultPresetIndex:"
- "getHIDDevices"
- "getHIDDevicesForMatching:"
- "getHIDElementForUsage:"
- "getSecurityToken:error:"
- "hasMatchingContainerID:containerID:"
- "hidDisplay"
- "init"
- "initWithBytes:length:"
- "initWithBytes:length:encoding:"
- "initWithContainerID:"
- "initWithDisplayDevice:index:"
- "initWithDomain:code:userInfo:"
- "initWithMatching:"
- "initWithService:"
- "integerValue"
- "invalidate:"
- "isEqualToString:"
- "length"
- "localizedStringForKey:value:table:"
- "logicalMax"
- "logicalMin"
- "lowercaseString"
- "mainBundle"
- "numberWithInteger:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "open"
- "presets"
- "q"
- "q24@0:8^@16"
- "registryID"
- "service"
- "set:error:"
- "setActivePresetIndex:error:"
- "setCancelHandler:"
- "setCurrentPresetIndex:error:"
- "setDataValue:"
- "setDevice:"
- "setDeviceMatching:"
- "setDispatchQueue:"
- "setHidDisplay:"
- "setInputDataHandler:"
- "setInputElementHandler:"
- "setInputElementMatching:"
- "setIntegerValue:"
- "setObject:forKeyedSubscript:"
- "setOutputData:error:"
- "setupIOReporting"
- "setupInterface"
- "setupPresets"
- "stringWithFormat:"
- "uniqueID"
- "usage"
- "usagePage"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "valid"
- "writable"

```
