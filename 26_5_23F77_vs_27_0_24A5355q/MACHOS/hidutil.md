## hidutil

> `/usr/bin/hidutil`

```diff

-2238.120.5.0.0
-  __TEXT.__text: 0x28ac
+2353.0.0.0.1
+  __TEXT.__text: 0x298c
   __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_stubs: 0x4a0
-  __TEXT.__const: 0x11e1
-  __TEXT.__cstring: 0x15df
-  __TEXT.__objc_classname: 0x1
+  __TEXT.__objc_stubs: 0x4e0
+  __TEXT.__const: 0x13e6
+  __TEXT.__cstring: 0x1840
   __TEXT.__gcc_except_tab: 0x24
-  __TEXT.__objc_methname: 0x315
+  __TEXT.__objc_methname: 0x34b
   __TEXT.__unwind_info: 0xf0
-  __DATA_CONST.__auth_got: 0x230
-  __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0x278
-  __DATA_CONST.__cfstring: 0x680
+  __DATA_CONST.__cfstring: 0x6e0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_selrefs: 0x128
+  __DATA_CONST.__auth_got: 0x230
+  __DATA_CONST.__got: 0x90
+  __DATA.__objc_selrefs: 0x138
   __DATA.__data: 0x164
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 85E6778E-DC63-350B-84C9-952FF82330A4
-  Functions: 34
-  Symbols:   94
-  CStrings:  182
+  UUID: 63CEFE1E-703B-35FB-A81A-5FD1546AD509
+  Functions: 37
+  Symbols:   95
+  CStrings:  190
 
Symbols:
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x24
CStrings:
+ "\nList HID Event System services and devices\n\nUsage:\n\n  hidutil list [--ndjson] [ --matching <matching> ]\n\nFlags:\n\n  -n  --ndjson................print service/device information in ndjson format\n  -m  --matching..............Set matching services/devices\n                              Input can be either json style dictionary or common\n                              device string e.g. keyboard, mouse, digitizer.\n                                  Supported properties:\n                                      ProductID        - numeric value (decimal or hex)\n                                      VendorID         - numeric value (decimal or hex)\n                                      LocationID       - numeric value (decimal or hex)\n                                      PrimaryUsagePage - numeric value (decimal or hex)\n                                      PrimaryUsage     - numeric value (decimal or hex)\n                                      Transport        - string value\n                                      Product          - string value\n                                  For matching against generic properties, you will need to include\n                                  the \"IOPropertyMatch\" key (see example below).\n                                  Example strings:\n                                      'keyboard'\n                                      'digi'\n                                      '{\"ProductID\":0x8600,\"VendorID\":0x5ac}'\n                                      '[{\"ProductID\":0x8600},{\"PrimaryUsagePage\":1,\"PrimaryUsage\":6}]'\n                                      '{\"IOPropertyMatch\":{\"ReportInterval\":1000}}'\n                                      '<dict><key>Transport</key><string>USB</string></dict>'\n\nExamples:\n\n  hidutil list\n  hidutil list --matching '{\"ProductID\":0x54c}'\n  hidutil list --matching '{\"ProductID\":0x54c,\"VendorID\":746}'\n  hidutil list --matching '<dict><key>Transport</key><string>USB</string></dict>'"
+ "\nRead/Write HID Event System property\n\nUsage:\n\n  hidutil property [ --matching <matching> ][ --get <key> ][ --set <key> ]\n\nFlags:\n\n  -g  --get...................Get property with key (where key is string value)\n  -s  --set...................Set property (JSON dictionary or plist dict body with <data> for binary values)\n  -m  --matching..............Set matching services/devices\n                              Input can be either json style dictionary or common\n                              device string e.g. keyboard, mouse, digitizer.\n                                  Supported properties:\n                                      ProductID        - numeric value (decimal or hex)\n                                      VendorID         - numeric value (decimal or hex)\n                                      LocationID       - numeric value (decimal or hex)\n                                      PrimaryUsagePage - numeric value (decimal or hex)\n                                      PrimaryUsage     - numeric value (decimal or hex)\n                                      Transport        - string value\n                                      Product          - string value\n                                  For matching against generic properties, you will need to include\n                                  the \"IOPropertyMatch\" key (see example below).\n                                  Example strings:\n                                      'keyboard'\n                                      'digi'\n                                      '{\"ProductID\":0x8600,\"VendorID\":0x5ac}'\n                                      '[{\"ProductID\":0x8600},{\"PrimaryUsagePage\":1,\"PrimaryUsage\":6}]'\n                                      '{\"IOPropertyMatch\":{\"ReportInterval\":1000}}'\n                                      '<dict><key>Transport</key><string>USB</string></dict>'\n\nExamples:\n\n  hidutil property --matching '{\"ProductID\":0x54c}' --get \"HIDPointerAcceleration\"\n  hidutil property --matching '{\"ProductID\":0x54c,\"VendorID\":746}' --set '{\"HIDPointerAcceleration\":0}'\n  hidutil property --matching '<dict><key>ProductID</key><integer>803</integer></dict>' --get \"HIDPointerAcceleration\"\n  hidutil property --get \"HIDPointerAcceleration\"\n  hidutil property --set '<dict><key>HIDPointerAccelerationTable</key><data>AAECBA==</data></dict>'"
+ "<"
+ "<plist version=\"1.0\">%@</plist>"
+ "HIDPropertiesRequiredForMatching"
+ "NSPropertyListSerialization %@"
+ "hasPrefix:"
+ "propertyListWithData:options:format:error:"
- "\nList HID Event System services and devices\n\nUsage:\n\n  hidutil list [--ndjson] [ --matching <matching> ]\n\nFlags:\n\n  -n  --ndjson................print service/device information in ndjson format\n  -m  --matching..............Set matching services/devices\n                              Input can be either json style dictionary or common\n                              device string e.g. keyboard, mouse, digitizer.\n                                  Supported properties:\n                                      ProductID        - numeric value (decimal or hex)\n                                      VendorID         - numeric value (decimal or hex)\n                                      LocationID       - numeric value (decimal or hex)\n                                      PrimaryUsagePage - numeric value (decimal or hex)\n                                      PrimaryUsage     - numeric value (decimal or hex)\n                                      Transport        - string value\n                                      Product          - string value\n                                  For matching against generic properties, you will need to include\n                                  the \"IOPropertyMatch\" key (see example below).\n                                  Example strings:\n                                      'keyboard'\n                                      'digi'\n                                      '{\"ProductID\":0x8600,\"VendorID\":0x5ac}'\n                                      '[{\"ProductID\":0x8600},{\"PrimaryUsagePage\":1,\"PrimaryUsage\":6}]'\n                                      '{\"IOPropertyMatch\":{\"ReportInterval\":1000}}'\n\nExamples:\n\n  hidutil list\n  hidutil list --matching '{\"ProductID\":0x54c}'\n  hidutil list --matching '{\"ProductID\":0x54c,\"VendorID\":746}'"
- "\nRead/Write HID Event System property\n\nUsage:\n\n  hidutil property [ --matching <matching> ][ --get <key> ][ --set <key> ]\n\nFlags:\n\n  -g  --get...................Get property with key (where key is string value)\n  -s  --set...................Set property (key/value pair JSON style dictionary)\n  -m  --matching..............Set matching services/devices\n                              Input can be either json style dictionary or common\n                              device string e.g. keyboard, mouse, digitizer.\n                                  Supported properties:\n                                      ProductID        - numeric value (decimal or hex)\n                                      VendorID         - numeric value (decimal or hex)\n                                      LocationID       - numeric value (decimal or hex)\n                                      PrimaryUsagePage - numeric value (decimal or hex)\n                                      PrimaryUsage     - numeric value (decimal or hex)\n                                      Transport        - string value\n                                      Product          - string value\n                                  For matching against generic properties, you will need to include\n                                  the \"IOPropertyMatch\" key (see example below).\n                                  Example strings:\n                                      'keyboard'\n                                      'digi'\n                                      '{\"ProductID\":0x8600,\"VendorID\":0x5ac}'\n                                      '[{\"ProductID\":0x8600},{\"PrimaryUsagePage\":1,\"PrimaryUsage\":6}]'\n                                      '{\"IOPropertyMatch\":{\"ReportInterval\":1000}}'\n\nExamples:\n\n  hidutil property --matching '{\"ProductID\":0x54c}' --get \"HIDPointerAcceleration\"\n  hidutil property --matching '{\"ProductID\":0x54c,\"VendorID\":746}' --set '{\"HIDPointerAcceleration\":0}'\n  hidutil property --get \"HIDPointerAcceleration\""
- "Hidden"

```
