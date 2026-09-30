## com.apple.driver.AppleHSBluetoothDriver

> `com.apple.driver.AppleHSBluetoothDriver`

```diff

 8420.1.0.0.0
   __TEXT.__cstring: 0x835
   __TEXT.__os_log: 0xa13
-  __TEXT_EXEC.__text: 0x8ec4
+  __TEXT.__const: 0x80
+  __TEXT_EXEC.__text: 0x925c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x128

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x2dd8
   __DATA_CONST.__kalloc_type: 0x100
-  UUID: A16E922A-6B4D-3DB6-8512-B876F62082C0
-  Functions: 142
-  Symbols:   723
+  UUID: 04500AC8-FEB9-3A51-9D04-E602935CFEF1
+  Functions: 146
+  Symbols:   730
   CStrings:  119
 
Symbols:
+ _ZN22AppleHSBluetoothDevice12handleReportEP18IOMemoryDescriptor15IOHIDReportTypej.cold.1
+ _ZN22AppleHSBluetoothDevice12handleReportEP18IOMemoryDescriptor15IOHIDReportTypej.cold.2
+ _ZN22AppleHSBluetoothDevice12handleReportEP18IOMemoryDescriptor15IOHIDReportTypej.cold.3
+ _ZN22AppleHSBluetoothDevice12handleReportEP18IOMemoryDescriptor15IOHIDReportTypej.cold.4
+ _ZN22AppleHSBluetoothDevice12handleReportEP18IOMemoryDescriptor15IOHIDReportTypej.cold.5
+ _ZNK7libkern17bounded_array_refIhN9os_detail21panic_trapping_policyEE5sliceEmm.cold.1
+ _ZNK7libkern17bounded_array_refIhN9os_detail21panic_trapping_policyEE5sliceEmm.cold.2
Functions:
~ __ZN19AppleHSBluetoothNub26HSBluetoothComparePropertyEP12OSDictionaryPK8OSSymbol : 264 -> 284
~ __ZN19AppleHSBluetoothNub41HSBluetoothComparePropertyInArrayWithMaskEP12OSDictionaryPKcS3_S3_Pj : 808 -> 804
~ __ZN25AppleHSBluetoothInterface5startEP9IOService : 1732 -> 1844
~ __ZN25AppleHSBluetoothInterface4freeEv : 28 -> 32
~ __ZN25AppleHSBluetoothInterface18matchPropertyTableEP12OSDictionaryPi : 3952 -> 3960
- __Z16OSDynamicPtrCastI8OSNumber8OSObjectE11OSSharedPtrIT_ERKS2_IT0_E
~ __ZN25AppleHSBluetoothInterface4initEPK32AppleHSBluetoothDeviceDescriptorPK35AppleHSBluetoothInterfaceDescriptor : 524 -> 540
~ __ZN25AppleHSBluetoothInterface5closeEP9IOServicej : 152 -> 160
~ __ZN22AppleHSBluetoothDeviceC2EPK11OSMetaClass : 96 -> 164
~ __ZN22AppleHSBluetoothDeviceD2Ev : 504 -> 516
~ __ZN22AppleHSBluetoothDeviceD1Ev : 504 -> 516
~ __ZN22AppleHSBluetoothDeviceC2Ev : 132 -> 200
~ __ZN22AppleHSBluetoothDevice4initEP12OSDictionary : 648 -> 660
~ __ZN22AppleHSBluetoothDevice4freeEv : 40 -> 44
~ __ZN22AppleHSBluetoothDevice21lockForControlRequestEv : 296 -> 300
~ __ZN22AppleHSBluetoothDevice12handleReportEP18IOMemoryDescriptor15IOHIDReportTypej : 2744 -> 3236
~ __ZNK7libkern17bounded_array_refIhN9os_detail21panic_trapping_policyEE5sliceEmm : 100 -> 72
~ __ZN22AppleHSBluetoothDevice14getReportGatedEP18IOMemoryDescriptor15IOHIDReportTypejh : 1404 -> 1424
~ __ZN25AppleHSBluetoothHIDDriver5startEP9IOService : 2560 -> 2640
- __Z16OSDynamicPtrCastI8OSNumber8OSObjectE11OSSharedPtrIT_ERKS2_IT0_E
~ __ZN25AppleHSBluetoothHIDDriver4freeEv : 132 -> 136
~ __ZNK25AppleHSBluetoothHIDDriver18newProductIDNumberEv : 108 -> 116
~ __ZNK25AppleHSBluetoothHIDDriver21newSerialNumberStringEv : 328 -> 348
~ __ZNK25AppleHSBluetoothHIDDriver16newProductStringEv : 108 -> 116
~ __ZNK25AppleHSBluetoothHIDDriver20newCountryCodeNumberEv : 84 -> 92
~ __ZNK25AppleHSBluetoothHIDDriver19newReportDescriptorEPP18IOMemoryDescriptor : 328 -> 348

```
