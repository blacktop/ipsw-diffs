## SystemStatus

> `/System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus`

```diff

-210.3.2.100.0
-  __TEXT.__text: 0x51fdc
-  __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_methlist: 0x713c
+210.4.10.0.0
+  __TEXT.__text: 0x53b88
+  __TEXT.__auth_stubs: 0x670
+  __TEXT.__objc_methlist: 0x7a78
   __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0x37ee
+  __TEXT.__cstring: 0x38e6
   __TEXT.__oslogstring: 0x128e
-  __TEXT.__gcc_except_tab: 0x43c
-  __TEXT.__unwind_info: 0x1ea8
-  __TEXT.__objc_classname: 0x1875
-  __TEXT.__objc_methname: 0x9de3
-  __TEXT.__objc_methtype: 0x158f
-  __TEXT.__objc_stubs: 0x53e0
-  __DATA_CONST.__got: 0x548
-  __DATA_CONST.__const: 0x1818
-  __DATA_CONST.__objc_classlist: 0x520
+  __TEXT.__gcc_except_tab: 0x444
+  __TEXT.__unwind_info: 0x1f58
+  __TEXT.__objc_classname: 0x18f3
+  __TEXT.__objc_methname: 0xa32c
+  __TEXT.__objc_methtype: 0x15f2
+  __TEXT.__objc_stubs: 0x54e0
+  __DATA_CONST.__got: 0x550
+  __DATA_CONST.__const: 0x1868
+  __DATA_CONST.__objc_classlist: 0x540
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bf0
+  __DATA_CONST.__objc_selrefs: 0x1d18
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x398
+  __DATA_CONST.__objc_superrefs: 0x3b8
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x340
+  __AUTH_CONST.__auth_got: 0x348
   __AUTH_CONST.__const: 0x800
-  __AUTH_CONST.__cfstring: 0x40a0
-  __AUTH_CONST.__objc_const: 0xe928
+  __AUTH_CONST.__cfstring: 0x4200
+  __AUTH_CONST.__objc_const: 0xe3d0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x498
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0x4bc
   __DATA.__data: 0xd28
-  __DATA_DIRTY.__objc_ivar: 0x98
+  __DATA_DIRTY.__objc_ivar: 0xa0
   __DATA_DIRTY.__objc_data: 0x32a0
   __DATA_DIRTY.__bss: 0x170
   __DATA_DIRTY.__common: 0x40

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2851
-  Symbols:   3577
-  CStrings:  2586
+  Functions: 2911
+  Symbols:   3664
+  CStrings:  2649
 
Symbols:
+ OBJC_IVAR_$_STBackgroundActivityVisualDescriptor._prefersToSuppressDefaultUserInteractionHandler
+ OBJC_IVAR_$_STStatusBarData._additionalEntries
+ OBJC_IVAR_$_STStatusBarData._externalBluetoothEntry
+ OBJC_IVAR_$_STStatusBarData._externalCellularEntry
+ OBJC_IVAR_$_STStatusBarData._externalWifiEntry
+ OBJC_IVAR_$_STStatusBarData._weatherEntry
+ _OBJC_CLASS_$_STStatusBarDataDictionaryEntry
+ _OBJC_CLASS_$_STStatusBarDataImageAndStringEntry
+ _OBJC_CLASS_$_STStatusBarDataPersonNameEntry
+ _OBJC_CLASS_$_STStatusBarDataWeatherEntry
+ _OBJC_METACLASS_$_STStatusBarDataDictionaryEntry
+ _OBJC_METACLASS_$_STStatusBarDataImageAndStringEntry
+ _OBJC_METACLASS_$_STStatusBarDataPersonNameEntry
+ _OBJC_METACLASS_$_STStatusBarDataWeatherEntry
+ _STStatusBarDataEntryAdditionalEntriesKey
+ _STStatusBarDataEntryExternalBluetoothKey
+ _STStatusBarDataEntryExternalCellularKey
+ _STStatusBarDataEntryExternalWifiKey
+ _STStatusBarDataEntryWeatherKey
+ _objc_retainAutoreleasedReturnValue
CStrings:
+ "\x052\x11"
+ "\x0f\x0f\x0f"
+ "@\"NSObject\"8@?0"
+ "@\"STStatusBarDataDictionaryEntry\""
+ "@\"STStatusBarDataPersonNameEntry\""
+ "@\"STStatusBarDataWeatherEntry\""
+ "PrefersToSuppressDefaultUserInteractionHandler"
+ "STStatusBarDataDictionaryEntry"
+ "STStatusBarDataImageAndStringEntry"
+ "STStatusBarDataPersonNameEntry"
+ "STStatusBarDataWeatherEntry"
+ "T@\"NSDictionary\",R,C,N,V_dictionary"
+ "T@\"NSString\",R,C,N,V_aqi"
+ "T@\"NSString\",R,C,N,V_avatarIdentifier"
+ "T@\"NSString\",R,C,N,V_temperature"
+ "T@\"STStatusBarDataBluetoothEntry\",R,N,V_externalBluetoothEntry"
+ "T@\"STStatusBarDataCellularEntry\",R,N,V_externalCellularEntry"
+ "T@\"STStatusBarDataDictionaryEntry\",C,D,N"
+ "T@\"STStatusBarDataDictionaryEntry\",R,N,V_additionalEntries"
+ "T@\"STStatusBarDataPersonNameEntry\",C,D,N"
+ "T@\"STStatusBarDataPersonNameEntry\",R,N,V_personNameEntry"
+ "T@\"STStatusBarDataWeatherEntry\",C,D,N"
+ "T@\"STStatusBarDataWeatherEntry\",R,N,V_weatherEntry"
+ "T@\"STStatusBarDataWifiEntry\",R,N,V_externalWifiEntry"
+ "TB,R,N,V_prefersToSuppressDefaultUserInteractionHandler"
+ "_additionalEntries"
+ "_aqi"
+ "_avatarIdentifier"
+ "_dictionary"
+ "_externalBluetoothEntry"
+ "_externalCellularEntry"
+ "_externalWifiEntry"
+ "_prefersToSuppressDefaultUserInteractionHandler"
+ "_temperature"
+ "_weatherEntry"
+ "additionalEntries"
+ "aqi"
+ "avatarIdentifier"
+ "decodeDictionaryOfClass:forKey:"
+ "decodeDictionaryWithKeysOfClasses:objectsOfClasses:forKey:"
+ "entryWithDictionary:"
+ "entryWithImageName:temperature:aqi:"
+ "entryWithImageNamed:stringValue:"
+ "entryWithStringValue:avatarIdentifier:"
+ "externalBluetoothEntry"
+ "externalCellularEntry"
+ "externalWifiEntry"
+ "prefersToSuppressDefaultUserInteractionHandler"
+ "setAdditionalEntries:"
+ "setExternalBluetoothEntry:"
+ "setExternalCellularEntry:"
+ "setExternalWifiEntry:"
+ "setPrefersToSuppressDefaultUserInteractionHandler:"
+ "setWeatherEntry:"
+ "temperature"
+ "weatherEntry"
- "\x053"
- "\x0f\x0f\n"
- "T@\"STStatusBarDataStringEntry\",R,N,V_personNameEntry"

```
