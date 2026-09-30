## com.apple.iokit.IOUSBHostFamily

> `com.apple.iokit.IOUSBHostFamily`

```diff

-1504.120.3.0.0
-  __TEXT.__cstring: 0xa0f2
-  __TEXT.__os_log: 0x8562
+1504.120.4.0.0
+  __TEXT.__cstring: 0xa116
+  __TEXT.__os_log: 0x8586
   __TEXT.__const: 0x2008
-  __TEXT_EXEC.__text: 0x91698
+  __TEXT_EXEC.__text: 0x918d0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1f0
   __DATA.__common: 0x920

   __DATA_CONST.__const: 0xc268
   __DATA_CONST.__kalloc_type: 0x1b00
   __DATA_CONST.__kalloc_var: 0x280
-  UUID: 69B3A7B6-DA1C-332D-B2F2-718A5D00B8A9
+  UUID: A7DB0FB9-53DA-3D87-A5CE-01436D5D22D1
   Functions: 1913
   Symbols:   0
-  CStrings:  1624
+  CStrings:  1626
 
Functions:
~ __ZN22AppleUSBHostController10createPipeEPKN11StandardUSB18EndpointDescriptorEPKNS0_23ConfigurationDescriptorEP15IOUSBHostDeviceP18IOUSBHostInterface : 1940 -> 2532
~ __ZN13IOUSBHostPipe28initWithDescriptorsAndOwnersEPKN11StandardUSB18EndpointDescriptorEPKNS0_23ConfigurationDescriptorEP22AppleUSBHostControllerP15IOUSBHostDeviceP18IOUSBHostInterfaceht : 1536 -> 1512
CStrings:
+ "%s@%s: %s::%s: invalid descriptors\n"

```
