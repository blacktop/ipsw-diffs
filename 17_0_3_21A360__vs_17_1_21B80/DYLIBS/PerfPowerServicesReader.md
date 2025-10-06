## PerfPowerServicesReader

> `/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader`

```diff

-1775.2.1.0.0
-  __TEXT.__text: 0x46ad8
+1787.40.67.0.0
+  __TEXT.__text: 0x46dc4
   __TEXT.__auth_stubs: 0xdb0
   __TEXT.__init_offsets: 0xdc
-  __TEXT.__objc_methlist: 0x1980
-  __TEXT.__const: 0x5fc2
+  __TEXT.__objc_methlist: 0x19d8
+  __TEXT.__const: 0x5fd2
   __TEXT.__cstring: 0x4e17
   __TEXT.__oslogstring: 0xa60
-  __TEXT.__gcc_except_tab: 0x3f44
-  __TEXT.__unwind_info: 0x289c
+  __TEXT.__gcc_except_tab: 0x3f5c
+  __TEXT.__unwind_info: 0x28b4
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x48a
-  __TEXT.__objc_methname: 0x3951
-  __TEXT.__objc_methtype: 0x99d
-  __TEXT.__objc_stubs: 0x2f60
+  __TEXT.__objc_classname: 0x4a9
+  __TEXT.__objc_methname: 0x39d5
+  __TEXT.__objc_methtype: 0x984
+  __TEXT.__objc_stubs: 0x2fe0
   __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__const: 0x348
-  __DATA_CONST.__objc_classlist: 0x158
+  __DATA_CONST.__const: 0x368
+  __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2438
-  __DATA_CONST.__objc_selrefs: 0xec0
+  __DATA_CONST.__objc_const: 0x2458
+  __DATA_CONST.__objc_selrefs: 0xee0
   __AUTH_CONST.__cfstring: 0x1680
-  __AUTH_CONST.__objc_const: 0x1278
+  __AUTH_CONST.__objc_const: 0x1308
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__const: 0x23e8
   __AUTH_CONST.__auth_got: 0x668
-  __AUTH.__objc_data: 0xd70
+  __AUTH.__objc_data: 0xdc0
   __AUTH.__const_weak: 0xc48
   __AUTH.__data: 0x28
   __AUTH.__got_weak: 0x88
   __DATA.__got_weak: 0x5c8
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x1f8
-  __DATA.__objc_superrefs: 0xf8
+  __DATA.__objc_classrefs: 0x200
+  __DATA.__objc_superrefs: 0x100
   __DATA.__objc_ivar: 0x18c
   __DATA.__data: 0xf99
-  __DATA.__bss: 0x88
+  __DATA.__bss: 0x98
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: B33D305C-E872-3617-8A7E-C6C6FC345E48
-  Functions: 2262
-  Symbols:   6635
-  CStrings:  1372
+  UUID: 995E6280-AB27-3F70-BF2D-DA56FD64C57F
+  Functions: 2269
+  Symbols:   6664
+  CStrings:  1377
 
Symbols:
+ +[PPSPredicateUtilities predicateForStartTimestamp:endTimestamp:withKeyPath:]
+ +[PPSTimestampConverterRegistry converterForFilepath:]
+ +[PPSTimestampConverterRegistry sharedInstance]
+ -[PPSTimestampConverterRegistry .cxx_destruct]
+ -[PPSTimestampConverterRegistry converters]
+ -[PPSTimestampConverterRegistry init]
+ -[PPSTimestampConverterRegistry setConverters:]
+ _OBJC_CLASS_$_PPSTimestampConverterRegistry
+ _OBJC_IVAR_$_PPSTimestampConverterRegistry._converters
+ _OBJC_METACLASS_$_PPSTimestampConverterRegistry
+ __OBJC_$_CLASS_METHODS_PPSTimestampConverterRegistry
+ __OBJC_$_INSTANCE_METHODS_PPSTimestampConverterRegistry
+ __OBJC_$_INSTANCE_VARIABLES_PPSTimestampConverterRegistry
+ __OBJC_$_PROP_LIST_PPSTimestampConverterRegistry
+ __OBJC_CLASS_RO_$_PPSTimestampConverterRegistry
+ __OBJC_METACLASS_RO_$_PPSTimestampConverterRegistry
+ ___47+[PPSTimestampConverterRegistry sharedInstance]_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ _objc_msgSend$converterForFilepath:
+ _objc_msgSend$converters
+ _objc_msgSend$getMetadataForSubsystem:category:name:
+ _objc_msgSend$monotonicTimeFromEpochTime:
+ _objc_msgSend$predicateForStartTimestamp:endTimestamp:withKeyPath:
+ _sharedInstance.instance
- +[PPSPredicateUtilities predicateForDateInterval:withKeyPath:]
- _OBJC_IVAR_$_PPSSQLiteTimeSeriesIngester._timestampConverter
- _objc_msgSend$predicateForDateInterval:withKeyPath:
CStrings:
+ "F"
+ "PPSTimestampConverterRegistry"
+ "T@\"NSMutableDictionary\",&,V_converters"
+ "_converters"
+ "converterForFilepath:"
+ "converters"
+ "getMetadataForSubsystem:category:name:"
+ "predicateForStartTimestamp:endTimestamp:withKeyPath:"
+ "setConverters:"
- "@\"PPSTimestampConverter\""
- "G"
- "_timestampConverter"
- "predicateForDateInterval:withKeyPath:"

```
