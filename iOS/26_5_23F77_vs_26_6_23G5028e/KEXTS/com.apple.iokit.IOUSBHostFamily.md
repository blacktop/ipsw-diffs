## com.apple.iokit.IOUSBHostFamily

> `com.apple.iokit.IOUSBHostFamily`

```diff

-1504.120.4.0.0
-  __TEXT.__cstring: 0xa116
+1504.160.4.0.0
+  __TEXT.__cstring: 0xa128
   __TEXT.__os_log: 0x8586
   __TEXT.__const: 0x2008
-  __TEXT_EXEC.__text: 0x918d0
+  __TEXT_EXEC.__text: 0x919c0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1f0
   __DATA.__common: 0x920

   __DATA_CONST.__const: 0xc268
   __DATA_CONST.__kalloc_type: 0x1b00
   __DATA_CONST.__kalloc_var: 0x280
-  UUID: A7DB0FB9-53DA-3D87-A5CE-01436D5D22D1
+  UUID: E0807A2D-94DD-3C5C-B1EA-6CC918A9CC70
   Functions: 1913
   Symbols:   0
-  CStrings:  1626
+  CStrings:  1627
 
Functions:
~ __ZN16AppleUSBHostPort15registerServiceEj : 4492 -> 4544
~ ____ZN16AppleUSBHostPort15registerServiceEj_block_invoke_2 : 1664 -> 1704
~ ____ZN16AppleUSBHostPort23enumerateDeviceCompleteEP15IOUSBHostDevicei_block_invoke : 6580 -> 6648
~ sub_fffffe000a199f30 -> sub_fffffe000a23a870 : 264 -> 300
~ __ZN17IOUSBHostIOSource12destroyGatedEv : 836 -> 880
CStrings:
+ "UsbDeviceFunction"

```
