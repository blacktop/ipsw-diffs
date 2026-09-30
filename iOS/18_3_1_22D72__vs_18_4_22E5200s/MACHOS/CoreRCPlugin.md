## CoreRCPlugin

> `/System/Library/HIDPlugins/SessionFilters/CoreRCPlugin.plugin/CoreRCPlugin`

```diff

-249.80.2.0.0
-  __TEXT.__text: 0x4cb8
-  __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_stubs: 0x7c0
-  __TEXT.__objc_methlist: 0x250
-  __TEXT.__const: 0x88
-  __TEXT.__objc_methname: 0xd90
-  __TEXT.__cstring: 0x202
-  __TEXT.__objc_classname: 0xe6
-  __TEXT.__objc_methtype: 0x5a9
-  __TEXT.__oslogstring: 0xaa7
-  __TEXT.__unwind_info: 0x108
-  __DATA_CONST.__auth_got: 0x2c8
+254.100.6.0.0
+  __TEXT.__text: 0x3d6c
+  __TEXT.__auth_stubs: 0x4f0
+  __TEXT.__objc_stubs: 0x7a0
+  __TEXT.__objc_methlist: 0x484
+  __TEXT.__const: 0x70
+  __TEXT.__cstring: 0x2b3
+  __TEXT.__oslogstring: 0x73d
+  __TEXT.__objc_methname: 0xc2e
+  __TEXT.__objc_classname: 0xc3
+  __TEXT.__objc_methtype: 0x555
+  __TEXT.__unwind_info: 0x128
+  __DATA_CONST.__auth_got: 0x280
   __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0xc0
-  __DATA_CONST.__cfstring: 0x300
-  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__const: 0x90
+  __DATA_CONST.__cfstring: 0x420
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x1260
-  __DATA.__objc_selrefs: 0x288
-  __DATA.__objc_ivar: 0x90
-  __DATA.__objc_data: 0x140
+  __DATA.__objc_const: 0xb78
+  __DATA.__objc_selrefs: 0x390
+  __DATA.__objc_ivar: 0x70
+  __DATA.__objc_data: 0xf0
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/PrivateFrameworks/CoreRC.framework/CoreRC
   - /System/Library/PrivateFrameworks/HID.framework/HID
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 93
-  Symbols:   137
-  CStrings:  355
+  Functions: 71
+  Symbols:   121
+  CStrings:  322
 
Symbols:
+ _IOAVVideoInterfaceCopyDisplayAttributes
+ _IOAVVideoInterfaceCreateWithService
+ _MGGetSInt32Answer
+ _OBJC_CLASS_$_CECEDIDAttributes
+ _OBJC_CLASS_$_NSAssertionHandler
+ ___IOAVClassMatching
+ __os_log_default
+ _objc_retain
- _CFDataGetBytePtr
- _CFDataGetLength
- _CFEqual
- _CoreRCPluginVersionNumber
- _CoreRCPluginVersionString
- _IOAVServiceCopyEDID
- _IOAVServiceCreateWithService
- _IOObjectIsEqualTo
- _IORegistryEntryGetParentEntry
- _OBJC_CLASS_$_CoreRCDisplayInterfaceProperties
- _OBJC_CLASS_$_NSConstantArray
- _OBJC_CLASS_$_NSConstantIntegerNumber
- _OBJC_CLASS_$_NSDictionary
- _OBJC_CLASS_$_NSNumber
- _OBJC_CLASS_$_NSString
- _OBJC_METACLASS_$_CoreRCDisplayInterfaceProperties
- __DefaultRuneLocale
- ___maskrune
- __os_log_debug_impl
- _objc_release_x27
- _objc_release_x28
- _objc_retain_x23
- _objc_retain_x27
- _usleep
CStrings:
+ "\x013"
+ " asDeferred:%s;"
+ " asleep:%s;"
+ " cecBus:%@;"
+ " cecEnabled:%s;"
+ " recentWake:%s;"
+ "(%d:%@) Brightness notification: %@  %s"
+ "Added CEC device (%@)"
+ "All CoreRCDisplays: %@"
+ "Bus removed that we dont have %@"
+ "CEC Disabled! EDID matched against %@"
+ "CoreRCDisplay.m"
+ "CoreRCPlugin.m"
+ "Created CoreRCDisplay %@"
+ "Current display state should be asleep, don't send active source"
+ "DeviceClassNumber"
+ "DisabledEDIDs"
+ "EDID %@\n"
+ "Error adding DCP driver matching notification 0x%x"
+ "Failed to add CEC device"
+ "Failed to add IOAVVideoInterface matching notification for analytics 0x%x"
+ "Failed to add IODPDevice matching notification for analytics 0x%x"
+ "HPD low at init, deferring active source"
+ "IOAVVideoInterface"
+ "IODPDevice"
+ "IOServicePublish"
+ "LegacyManufacturerID"
+ "Link state %s on bus %@ (%@)\n"
+ "N"
+ "No CEC device %@"
+ "Not sending active source %@"
+ "PCON %@\n"
+ "Policy updated _cecEnabled: %d"
+ "ProductAttributes"
+ "ProductID"
+ "ProductName"
+ "Same bus re-added %@"
+ "UUIDString"
+ "WeekOfManufacture"
+ "Y"
+ "YearOfManufacture"
+ "_activeSourceDeferred"
+ "_cecEnabled"
+ "_iteratorCEC"
+ "_iteratorEDID"
+ "_iteratorPCON"
+ "cecBus is null"
+ "cecDevice"
+ "currentHandler"
+ "edidAttributes"
+ "handleFailureInMethod:object:file:lineNumber:description:"
+ "iPad"
+ "iPhone"
+ "initWithModelName:"
+ "initWithVendorID:"
+ "modelName"
+ "productID"
+ "queue is null"
+ "removeFromBus"
+ "sendEDIDAnalyticsForService:"
+ "sendPCONAnalyticsForService:"
+ "serviceNotificationAnalyticsEDID service published: 0x%llX : %s"
+ "serviceNotificationAnalyticsPCON service published: 0x%llX : %s"
+ "setObject:forKey:"
+ "sleepDisplay"
+ "uniqueID"
+ "updatePolicy"
+ "updatePolicy edid attributes not present"
+ "uuid"
+ "vendorID"
+ "week"
+ "year"
+ "\x81"
- "\x014"
- " avService: 0x%x"
- " role: %@;"
- "\""
- "(%d) Brightness notification: %@  %s"
- "(0x%llx)"
- "; cecService: 0x%x"
- "; standbyDisabled: %u;"
- "@\"NSDictionary\""
- "@\"NSString\""
- "@20@0:8I16"
- "@32@0:8@16^@24"
- "Added avService to %@"
- "Added cecService to %@"
- "All services terminated from interface, removing"
- "Apple"
- "B20@0:8B16"
- "CoreRCDisplayInterfaceProperties"
- "Could not find IOAVService"
- "Created CoreRCDisplay %@ (%@)"
- "DCPAVServiceProxy"
- "Disabling standby on %@"
- "Disabling standby on all displays"
- "Display is asleep, don't wake up TV"
- "EDID too short %ld"
- "EDID vendorID: %X, productID: %X, week: %d, year: %d, name: %s"
- "Enabling standby on %@"
- "Enabling standby on all displays"
- "External"
- "Failed to add CEC device, deferring: %@"
- "Failed to add DCP driver matching notification 0x%x"
- "Failed to add DCP driver termination notification 0x%x"
- "Failed to add DCPAVServiceProxy matching notification for EDID 0x%x"
- "Failed to add DCPAVServiceProxy termination notification for EDID 0x%x"
- "Failed to get AFK endpoint node 0x%X"
- "Failed to get DCPEXT node 0x%X"
- "Failed to get EDID 0x%X"
- "Failed to get RTBuddy endpoint node 0x%X"
- "Failed to get data pointer 0x%X"
- "Failed to get epic node 0x%X"
- "HDMI cable is not plugged in yet or TV is not ready, try again on HPD high."
- "I16@0:8"
- "IOServiceTerminate"
- "Link state %s (%@)\n"
- "Location"
- "Not Present"
- "Not sending active source _needToSendActiveSource: %d, _recentDisplayWake: %d, cecDevice: %@, err: %@"
- "Not sendings standby because it is disabled"
- "Removing avService from %@"
- "Removing cecService from %@"
- "Sending analytics %@\n"
- "Standby still disabled because of %@"
- "Successfully added CEC device (%@)"
- "T@\"NSDictionary\",&,N,V_properties"
- "T@\"NSString\",&,N,V_role"
- "TB,N,V_standbyDisabled"
- "TI,N,V_avService"
- "TI,N,V_cecService"
- "Unable to find interface with service: 0x%x"
- "Unable to get role"
- "_analyticsDelay"
- "_avService"
- "_cecService"
- "_interfaces"
- "_iteratorCECPublish"
- "_iteratorCECTermination"
- "_iteratorEDIDPublish"
- "_iteratorEDIDTermination"
- "_needToSendActiveSource"
- "_properties"
- "_role"
- "_standbyDisabled"
- "addCECDeviceToBus:error:"
- "addInterfacePropertiesForService:"
- "analyticsDelay"
- "avService"
- "cecService"
- "containsObject:"
- "dictionaryWithObjects:forKeys:count:"
- "getEDIDPropertiesForService:"
- "i"
- "numberWithUnsignedChar:"
- "numberWithUnsignedShort:"
- "properties"
- "removeInterfacePropertiesForService:"
- "role"
- "sending active source"
- "serviceNotificationCallbackCEC"
- "serviceNotificationCallbackEDID"
- "serviceNotificationCallbackEDID service published: 0x%x, location: %@ : %s"
- "setAvService:"
- "setCecService:"
- "setProperties:"
- "setRole:"
- "setStandbyDisabled:"
- "sleepDisplay:"
- "standbyDisabled"
- "stringWithCString:encoding:"
- "syncNotificationFromHotplug"
- "terminationNotificationCallbackCEC"
- "terminationNotificationCallbackEDID"
- "updateDisabledStateOnInterface properties no present"
- "updateDisabledStateOnInterface:"
- "v20@0:8B16"
- "\xa1"

```
