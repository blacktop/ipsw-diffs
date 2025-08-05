## GameControllerFoundation

> `/System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation`

```diff

-13.0.36.0.0
-  __TEXT.__text: 0x6e68c
+13.0.39.0.0
+  __TEXT.__text: 0x6e86c
   __TEXT.__auth_stubs: 0x1440
   __TEXT.__objc_methlist: 0x68dc
-  __TEXT.__const: 0x118
-  __TEXT.__gcc_except_tab: 0x32e8
+  __TEXT.__const: 0x120
+  __TEXT.__gcc_except_tab: 0x32fc
   __TEXT.__cstring: 0x6fb7
-  __TEXT.__oslogstring: 0x30a9
+  __TEXT.__oslogstring: 0x3171
   __TEXT.__ustring: 0x58
   __TEXT.__unwind_info: 0x20a8
   __TEXT.__eh_frame: 0x48

   __DATA.__objc_ivar: 0x854
   __DATA.__data: 0x1080
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x148
+  __DATA.__bss: 0x138
   __DATA_DIRTY.__objc_data: 0x500
-  __DATA_DIRTY.__bss: 0x58
+  __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4C84F8C5-E07D-36B3-B269-C5FEE3C57D95
+  UUID: 5582754A-23D7-3B3A-AE4F-9DBD9BA33E49
   Functions: 2849
   Symbols:   9836
-  CStrings:  4302
+  CStrings:  4303
 
Functions:
~ ___HIDDevicesMatched : 2660 -> 3100
~ ___ServiceMatchedCallback : 344 -> 364
~ ___ServiceRemovedCallback : 336 -> 356
CStrings:
+ "Check <IOHIDDevice %#llx> is a supported game controller {\n\t vendorID = %zu,\n\t productID = %zu,\n\t version = %zu,\n\t manufacturer = '%{public}@',\n\t product = '%{public}@',\n\t transport = '%{public}@',\n}"

```
