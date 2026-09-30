## wifivelocityd

> `/usr/libexec/wifivelocityd`

```diff

-1166.1.0.0.0
-  __TEXT.__text: 0x9d4cc
-  __TEXT.__auth_stubs: 0x13f0
-  __TEXT.__objc_stubs: 0xd320
-  __TEXT.__objc_methlist: 0x53e4
+1180.12.0.0.0
+  __TEXT.__text: 0x9f5e4
+  __TEXT.__auth_stubs: 0x1360
+  __TEXT.__objc_stubs: 0xd260
+  __TEXT.__objc_methlist: 0x53d4
   __TEXT.__dlopen_cstrs: 0x31a
-  __TEXT.__const: 0x398
-  __TEXT.__gcc_except_tab: 0x1914
-  __TEXT.__objc_methname: 0xddf9
-  __TEXT.__oslogstring: 0xb26e
-  __TEXT.__cstring: 0xc546
+  __TEXT.__const: 0x390
+  __TEXT.__gcc_except_tab: 0x189c
+  __TEXT.__objc_methname: 0xddab
+  __TEXT.__oslogstring: 0xb560
+  __TEXT.__cstring: 0xc580
   __TEXT.__objc_classname: 0x832
-  __TEXT.__objc_methtype: 0x23e9
+  __TEXT.__objc_methtype: 0x23f7
   __TEXT.__ustring: 0x8c
-  __TEXT.__unwind_info: 0x1b88
-  __DATA_CONST.__auth_got: 0xa08
-  __DATA_CONST.__got: 0x590
+  __TEXT.__unwind_info: 0x1d98
+  __DATA_CONST.__auth_got: 0x9c0
+  __DATA_CONST.__got: 0x588
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x29b8
-  __DATA_CONST.__cfstring: 0xafc0
+  __DATA_CONST.__const: 0x2990
+  __DATA_CONST.__cfstring: 0xaf20
   __DATA_CONST.__objc_classlist: 0x258
-  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28

   __DATA_CONST.__objc_intobj: 0xe88
   __DATA_CONST.__objc_arraydata: 0x23a0
   __DATA_CONST.__objc_dictobj: 0x14f0
-  __DATA_CONST.__objc_arrayobj: 0x14e8
+  __DATA_CONST.__objc_arrayobj: 0x14d0
   __DATA_CONST.__objc_doubleobj: 0x80
-  __DATA.__objc_const: 0x8be0
-  __DATA.__objc_selrefs: 0x3ae8
-  __DATA.__objc_ivar: 0x6e4
+  __DATA.__objc_const: 0x8b30
+  __DATA.__objc_selrefs: 0x3ac8
+  __DATA.__objc_ivar: 0x6d8
   __DATA.__objc_data: 0x1770
   __DATA.__data: 0x660
   __DATA.__bss: 0x140

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
   - @rpath/BloodhoundKit.framework/BloodhoundKit
-  UUID: F228E9CD-C138-391D-A6A3-63340F870F33
-  Functions: 2365
-  Symbols:   510
-  CStrings:  6749
+  UUID: 300A4D8E-D779-387C-AF06-9102A071C922
+  Functions: 2347
+  Symbols:   500
+  CStrings:  6743
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _OBJC_CLASS_$_NSManagedObject
- __os_log_fault_impl
- _class_copyPropertyList
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
- _property_getAttributes
- _property_getName
CStrings:
+ "-[W5LogManager __safeOffsetInFileForHandle:]"
+ "-[W5LogManager __safeSeekToEndOfFileForHandle:]"
+ "-[W5LogManager __safeSeekToFileOffset:forHandle:]"
+ "-[W5LogManager __safeWriteData:toHandle:]"
+ "/Library/Logs/com.apple.WiFiPolicy/airplane-wifi"
+ "17.171.99.36"
+ "17.253.119.201"
+ "17.253.119.202"
+ "17.32.194.15"
+ "17.47.160.185"
+ "B32@0:8Q16@24"
+ "[wifivelocity] %s (%s:%u) Failed to seek to offset %llu in fileHandle"
+ "[wifivelocity] %s (%s:%u) Failed to write header to fileHandle, aborting tool execution"
+ "[wifivelocity] %s (%s:%u) Failed to write timestamp placeholder to fileHandle"
+ "[wifivelocity] %s (%s:%u) [NSFileHandle offsetInFile] failed with exception %{public}@"
+ "[wifivelocity] %s (%s:%u) [NSFileHandle seekToEndOfFile] failed with exception %{public}@"
+ "[wifivelocity] %s (%s:%u) [NSFileHandle seekToFileOffset:] failed with exception %{public}@"
+ "[wifivelocity] %s (%s:%u) __safeOffsetInFileForHandle invalid fileHandle, exiting"
+ "[wifivelocity] %s (%s:%u) __safeSeekToEndOfFileForHandle invalid fileHandle, exiting"
+ "[wifivelocity] %s (%s:%u) __safeSeekToFileOffset invalid fileHandle, exiting"
+ "[wifivelocity] %s (%s:%u) __safeWriteData invalid fileHandle or data, exiting"
+ "[wifivelocity] %s (%s:%u) fileHandle is nil, cannot proceed with tool execution"
+ "^airplane-wifi"
+ "__safeOffsetInFileForHandle:"
+ "__safeSeekToEndOfFileForHandle:"
+ "__safeSeekToFileOffset:forHandle:"
+ "__safeWriteData:toHandle:"
+ "airplane-wifi-logs"
+ "setLogRedactionDisabled:"
- ",R"
- "-[NSManagedObject(WiFiVelocity) _w5DictionaryRepresentation]"
- "-dbg=print_nan_avail"
- "-nan"
- "-nan_peers"
- "17.254.0.22"
- "17.254.0.23"
- "17.254.0.34"
- "17.254.0.35"
- "Faulting"
- "Filtered known networks for customer install without MegaWiFi profile\n"
- "NSManagedObject+WiFiVelocity.m"
- "T:"
- "T@\"W5WiFiInterface\",R,&,V_nan"
- "Unexpected non secure codeable object: %@ in results (%lu) for request: %@"
- "[wifivelocity] %s (%s:%u) Ignoring non secure codeable object (%@) for %@: %@"
- "__startNANPerfLogging"
- "__startNANQueryTimer"
- "_nan"
- "_nanQueryFileHandle"
- "_nanQueryTimer"
- "_w5AllAttributes"
- "_w5DictionaryRepresentation"
- "defaultCStringEncoding"
- "entity"
- "eventType"
- "isSubclassOfClass:"
- "nan"
- "nan_%@"
- "valueForKey:"

```
