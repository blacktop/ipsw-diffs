## BackBoardServices

> `/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_floatobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-868.0.0.0.0
-  __TEXT.__text: 0x897a4
-  __TEXT.__objc_methlist: 0x8ca4
-  __TEXT.__const: 0x3e8
+873.100.0.0.0
+  __TEXT.__text: 0x8a250
+  __TEXT.__objc_methlist: 0x8d94
+  __TEXT.__const: 0x3f8
   __TEXT.__dlopen_cstrs: 0x18e
   __TEXT.__gcc_except_tab: 0x558
-  __TEXT.__cstring: 0xb8c3
-  __TEXT.__oslogstring: 0x2651
+  __TEXT.__cstring: 0xba23
+  __TEXT.__oslogstring: 0x26b6
   __TEXT.__ustring: 0x14
-  __TEXT.__unwind_info: 0x2368
+  __TEXT.__unwind_info: 0x2388
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1938
-  __DATA_CONST.__objc_classlist: 0x5e0
+  __DATA_CONST.__const: 0x1948
+  __DATA_CONST.__objc_classlist: 0x5f0
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3078
+  __DATA_CONST.__objc_selrefs: 0x30a0
   __DATA_CONST.__objc_protorefs: 0xe8
-  __DATA_CONST.__objc_superrefs: 0x418
+  __DATA_CONST.__objc_superrefs: 0x420
   __DATA_CONST.__objc_arraydata: 0x70
-  __DATA_CONST.__got: 0x7d0
-  __AUTH_CONST.__const: 0x1608
-  __AUTH_CONST.__cfstring: 0xa2a0
-  __AUTH_CONST.__objc_const: 0x121b8
+  __DATA_CONST.__got: 0x7e0
+  __AUTH_CONST.__const: 0x1628
+  __AUTH_CONST.__cfstring: 0xa400
+  __AUTH_CONST.__objc_const: 0x123c0
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x760
-  __AUTH.__objc_data: 0x2440
-  __DATA.__objc_ivar: 0x918
+  __AUTH.__objc_data: 0x24e0
+  __DATA.__objc_ivar: 0x924
   __DATA.__data: 0x14b0
-  __DATA.__bss: 0x5f0
+  __DATA.__bss: 0x600
   __DATA_DIRTY.__objc_data: 0x1680
   __DATA_DIRTY.__data: 0x50
   __DATA_DIRTY.__bss: 0x1d0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3466
-  Symbols:   7533
-  CStrings:  1944
+  Functions: 3485
+  Symbols:   7573
+  CStrings:  1957
 
Symbols:
+ +[BKSHardwareButtonLongPressDescriptor supportsSecureCoding]
+ +[BKSHardwareButtonService sharedInstance]
+ -[BKSHIDTouchRoutingPolicy setAvoidCancelingContinuingClients:]
+ -[BKSHIDTouchRoutingPolicy shouldAvoidCancelingContinuingClients]
+ -[BKSHardwareButtonLongPressDescriptor copyWithZone:]
+ -[BKSHardwareButtonLongPressDescriptor copy]
+ -[BKSHardwareButtonLongPressDescriptor description]
+ -[BKSHardwareButtonLongPressDescriptor encodeWithCoder:]
+ -[BKSHardwareButtonLongPressDescriptor hash]
+ -[BKSHardwareButtonLongPressDescriptor initWithCoder:]
+ -[BKSHardwareButtonLongPressDescriptor initWithPage:usage:timeout:]
+ -[BKSHardwareButtonLongPressDescriptor isEqual:]
+ -[BKSHardwareButtonLongPressDescriptor page]
+ -[BKSHardwareButtonLongPressDescriptor timeout]
+ -[BKSHardwareButtonLongPressDescriptor usage]
+ -[BKSHardwareButtonService setLongPressTimeouts:]
+ GCC_except_table1212
+ GCC_except_table1231
+ GCC_except_table1232
+ GCC_except_table1348
+ GCC_except_table136
+ GCC_except_table1372
+ GCC_except_table1395
+ GCC_except_table1569
+ GCC_except_table1574
+ GCC_except_table1584
+ GCC_except_table1722
+ GCC_except_table1831
+ GCC_except_table1964
+ GCC_except_table2092
+ GCC_except_table2101
+ GCC_except_table2230
+ GCC_except_table2344
+ GCC_except_table2346
+ GCC_except_table2392
+ GCC_except_table2623
+ GCC_except_table2817
+ GCC_except_table2824
+ GCC_except_table286
+ GCC_except_table287
+ GCC_except_table3138
+ GCC_except_table3164
+ GCC_except_table3326
+ GCC_except_table3360
+ GCC_except_table3361
+ _OBJC_CLASS_$_BKSHardwareButtonLongPressDescriptor
+ _OBJC_CLASS_$_BKSHardwareButtonService
+ _OBJC_IVAR_$_BKSHardwareButtonLongPressDescriptor._page
+ _OBJC_IVAR_$_BKSHardwareButtonLongPressDescriptor._timeout
+ _OBJC_IVAR_$_BKSHardwareButtonLongPressDescriptor._usage
+ _OBJC_METACLASS_$_BKSHardwareButtonLongPressDescriptor
+ _OBJC_METACLASS_$_BKSHardwareButtonService
+ __BKSHIDServicesSetButtonLongPressTimeouts
+ __BKSHIDSetButtonLongPressTimeouts
+ __OBJC_$_CLASS_METHODS_BKSHardwareButtonLongPressDescriptor
+ __OBJC_$_CLASS_METHODS_BKSHardwareButtonService
+ __OBJC_$_CLASS_PROP_LIST_BKSHardwareButtonLongPressDescriptor
+ __OBJC_$_INSTANCE_METHODS_BKSHardwareButtonLongPressDescriptor
+ __OBJC_$_INSTANCE_METHODS_BKSHardwareButtonService
+ __OBJC_$_INSTANCE_VARIABLES_BKSHardwareButtonLongPressDescriptor
+ __OBJC_$_PROP_LIST_BKSHardwareButtonLongPressDescriptor
+ __OBJC_CLASS_PROTOCOLS_$_BKSHardwareButtonLongPressDescriptor
+ __OBJC_CLASS_RO_$_BKSHardwareButtonLongPressDescriptor
+ __OBJC_CLASS_RO_$_BKSHardwareButtonService
+ __OBJC_METACLASS_RO_$_BKSHardwareButtonLongPressDescriptor
+ __OBJC_METACLASS_RO_$_BKSHardwareButtonService
+ ___42+[BKSHardwareButtonService sharedInstance]_block_invoke
+ _objc_msgSend$setAvoidCancelingContinuingClients:
+ _objc_msgSend$shouldAvoidCancelingContinuingClients
- GCC_except_table1209
- GCC_except_table1226
- GCC_except_table1228
- GCC_except_table134
- GCC_except_table1345
- GCC_except_table1369
- GCC_except_table1392
- GCC_except_table1566
- GCC_except_table1571
- GCC_except_table1581
- GCC_except_table1719
- GCC_except_table1828
- GCC_except_table1961
- GCC_except_table2089
- GCC_except_table2098
- GCC_except_table2227
- GCC_except_table2341
- GCC_except_table2343
- GCC_except_table2389
- GCC_except_table2620
- GCC_except_table2814
- GCC_except_table2821
- GCC_except_table283
- GCC_except_table284
- GCC_except_table3135
- GCC_except_table3161
- GCC_except_table3323
- GCC_except_table3357
- GCC_except_table3358
CStrings:
+ "<%@: %p 0x%X/0x%X timeout:%.3gs>"
+ "BKSHardwareButtonLongPressDescriptor.m"
+ "BKSSystemShellDidReconnect-21000327"
+ "ConfigA"
+ "ConfigB"
+ "Error encoding button long press timeouts: %{public}@"
+ "Error setting button long press timeouts: 0x%x"
+ "Failed to decode BKSHardwareButtonLongPressDescriptor: timeout <= 0"
+ "Failed to decode BKSHardwareButtonLongPressDescriptor: zero page"
+ "Failed to decode BKSHardwareButtonLongPressDescriptor: zero usage"
+ "avoidCancelingContinuingClients"
+ "backboardd-attr-cache-21000327"
+ "page != 0"
+ "timeout > 0"
+ "usage != 0"
- "BKSSystemShellDidReconnect-21000325"
- "backboardd-attr-cache-21000325"
```
