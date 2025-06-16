## sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

-1295.120.6.0.0
-  __TEXT.__text: 0x2ef54
-  __TEXT.__auth_stubs: 0xa00
-  __TEXT.__objc_stubs: 0xdc0
-  __TEXT.__objc_methlist: 0x2ec
-  __TEXT.__const: 0xf4
+1295.140.4.0.1
+  __TEXT.__text: 0x30ed8
+  __TEXT.__auth_stubs: 0xad0
+  __TEXT.__objc_stubs: 0x1220
+  __TEXT.__objc_methlist: 0x4c0
+  __TEXT.__const: 0x300
   __TEXT.__gcc_except_tab: 0x400
-  __TEXT.__oslogstring: 0x179d
-  __TEXT.__cstring: 0x292db
-  __TEXT.__objc_classname: 0x37
-  __TEXT.__objc_methname: 0xd5a
-  __TEXT.__objc_methtype: 0x159
-  __TEXT.__unwind_info: 0x408
-  __DATA_CONST.__auth_got: 0x510
+  __TEXT.__oslogstring: 0x1d5a
+  __TEXT.__cstring: 0x294b3
+  __TEXT.__objc_classname: 0xc4
+  __TEXT.__objc_methname: 0x1270
+  __TEXT.__objc_methtype: 0x275
+  __TEXT.__unwind_info: 0x484
+  __DATA_CONST.__auth_got: 0x578
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__auth_ptr: 0x80
-  __DATA_CONST.__const: 0x4c8
-  __DATA_CONST.__cfstring: 0x14e0
-  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__const: 0x508
+  __DATA_CONST.__cfstring: 0x1720
+  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0xb0
-  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0xe0
+  __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x190
-  __DATA.__objc_selrefs: 0x390
-  __DATA.__objc_ivar: 0x8
-  __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x3f8
-  __DATA.__bss: 0x10
+  __DATA_CONST.__objc_intobj: 0x48
+  __DATA.__objc_const: 0x718
+  __DATA.__objc_selrefs: 0x4e8
+  __DATA.__objc_ivar: 0x38
+  __DATA.__objc_data: 0x1e0
+  __DATA.__data: 0x4b8
+  __DATA.__bss: 0x30
   __DATA.__common: 0x62
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/CoreCaptureControl.framework/CoreCaptureControl
   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
+  - /System/Library/PrivateFrameworks/HID.framework/HID
   - /System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/NearField.framework/NearField

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libtzupdate.dylib
-  UUID: 30C09B56-22DA-3960-97D2-BC6756FCB015
-  Functions: 237
-  Symbols:   215
-  CStrings:  3588
+  UUID: AF60ED0C-6F3B-3F57-AB3B-C39EE7EE1670
+  Functions: 285
+  Symbols:   232
+  CStrings:  3743
 
Symbols:
+ _CFNotificationCenterAddObserver
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _CFNotificationCenterRemoveObserver
+ _NSStringFromClass
+ _NSStringFromSelector
+ _OBJC_CLASS_$_HIDEventSystemClient
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateFormatter
+ ___strlcpy_chk
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_wait
+ _mach_error_string
+ _objc_retain_x5
+ _os_log_create
CStrings:
+ "\x01\x11"
+ "\x11"
+ "\x12"
+ "%@"
+ "%@, directory %@, options %lu"
+ "%@/PalmspringCrashlog_%@_%@.%@"
+ "(%@, Palmspring Crashlog Header: [blob version: %d])"
+ "(Palmspring Crashlog Info Entry: [ID: %d, type: %d, header+raw blob size: %d, name: %@])"
+ "@\"NSData\""
+ "@\"NSMutableArray\""
+ "@\"NSObject<OS_dispatch_group>\""
+ "@\"NSObject<OS_os_log>\""
+ "@\"NSString\""
+ "@\"PalmspringCrashlogInfoEntry\""
+ "@24@0:8@16"
+ "@24@0:8^{_NSZone=}16"
+ "@32@0:8@16@24"
+ "@36@0:8C16C20I24@28"
+ "AppleDeviceManagementHIDDiagnostics"
+ "AppleDeviceManagementHIDDiagnostics class not found on this platform, failing HIDCrashlogsTaskWithDir"
+ "B40@0:8@16Q24^@32"
+ "B56@0:8@16@24@32Q40^@48"
+ "C"
+ "C16@0:8"
+ "CRC (0x%04x) of crashlog %@ did not match CRC in header (0x%04x)"
+ "Collected HID device diagnostics - %@"
+ "Collecting HID device diagnostics and saving it to directory %@"
+ "Collecting error stats and writing to directory %@"
+ "Crashlog %@ with type %@ received via notification"
+ "Crashlog (%d) does not have a full header: header size %ld, crashlog header+blob size %d"
+ "Crashlog (%d) header: blob version %d, type %d, blob size %d, crc16 0x%04x"
+ "Crashlog info did not contain the report ID and full header (bytes: %ld, report ID + header size: %lu)"
+ "Crashlog info report header extracted: version %d, # of crashlogs %d"
+ "Done waiting for crashlog extraction notifications, total time elapsed: %f ms"
+ "Failed to create directory %@: error %@"
+ "Failed to extract error stats from service 0x%llX"
+ "Get property on service 0x%llX performed to collect error stats, ret: %s"
+ "HIDCrashlogsTaskWithDir SPI timed out"
+ "HIDCrashlogsTaskWithDir:withTimeout:"
+ "I"
+ "I16@0:8"
+ "NSCopying"
+ "NSFastEnumeration"
+ "PalmspringCrashlog"
+ "PalmspringCrashlogFetchLastCrashlog"
+ "PalmspringCrashlogInfo"
+ "PalmspringCrashlogInfoEntry"
+ "PalmspringCrashlogRequestErrorStats"
+ "PrimaryUsage"
+ "PrimaryUsagePage"
+ "Q40@0:8^{?=Q^@^Q[5Q]}16^@24Q32"
+ "Received crashlog info report does not contain the expected amount of bytes based on the header (received %ld, expected %d)"
+ "Received unknown object in notification callback"
+ "Size of crashlog did not match expected size: header+blob (expected: %ld / actual: %d), blob (expected: %ld, actual %d)"
+ "Successful extraction of error stats from service 0x%llX"
+ "T@\"NSData\",R,C,N,V_data"
+ "T@\"NSMutableArray\",R,N,V_entries"
+ "T@\"NSObject<OS_dispatch_group>\",R,V_dispatchGroup"
+ "T@\"NSObject<OS_os_log>\",R"
+ "T@\"NSString\",R,N"
+ "T@\"NSString\",R,N,V_name"
+ "T@\"NSString\",R,V_directory"
+ "T@\"PalmspringCrashlogInfoEntry\",R,C,N,V_info"
+ "TC,R,N,V_blobVersion"
+ "TC,R,N,V_type"
+ "TC,R,N,V_uniqueID"
+ "TC,R,N,V_version"
+ "TI,R,N"
+ "TI,R,N,V_headerAndRawBlobSize"
+ "Waiting to receive notifications from crashlog extraction..."
+ "Writing crashlog %@ to %@ %@, error %@"
+ "_blobVersion"
+ "_data"
+ "_directory"
+ "_dispatchGroup"
+ "_entries"
+ "_headerAndRawBlobSize"
+ "_info"
+ "_log"
+ "_name"
+ "_type"
+ "_uniqueID"
+ "_version"
+ "allocWithZone:"
+ "blobVersion"
+ "bytes"
+ "collectDiagnosticsAndWriteToDirectory:"
+ "collectErrorStats"
+ "com.apple.hid.AppleTopCase"
+ "com.apple.hidswdebug.AppleDeviceManagementHIDFilter.CrashlogExtracted"
+ "copyWithZone:"
+ "crash"
+ "crashlogData"
+ "crashlogName"
+ "crashlogPathExtension"
+ "crashlogType"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "data"
+ "date"
+ "directory"
+ "dispatchGroup"
+ "entries"
+ "failed"
+ "failure"
+ "handleExtractedErrorStats:"
+ "headerAndRawBlobSize"
+ "i"
+ "info"
+ "initWithData:"
+ "initWithInfoEntry:data:"
+ "initWithOutputDirectory:"
+ "initWithType:"
+ "initWithUniqueID:type:headerAndRawBlobSize:name:"
+ "isEqualToNumber:"
+ "log"
+ "maxInfoReportSize"
+ "name"
+ "objectForKeyedSubscript:"
+ "propertyForKey:"
+ "serviceID"
+ "services"
+ "setDateFormat:"
+ "setMatching:"
+ "stringFromDate:"
+ "stringWithCString:encoding:"
+ "stringWithFormat:"
+ "subdataWithRange:"
+ "succeeded"
+ "success"
+ "timeIntervalSinceNow"
+ "type"
+ "uniqueID"
+ "writeToDirectory:crashlogData:name:options:error:"
+ "writeToDirectory:options:error:"
+ "writeToFile:options:error:"
+ "yyyy-MM-dd-HH:mm:ss"

```
