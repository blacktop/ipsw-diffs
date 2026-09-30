## USBGenericPrintingClass

> `/System/Library/Printers/Libraries/USBGenericPrintingClass.plugin/Contents/MacOS/USBGenericPrintingClass`

```diff

-740.0.0.0.0
-  __TEXT.__text: 0x2b68 sha256:8bd4e64b4031a4529913fbd208e0aeef51c49106dd7e6d9123790bdb5ca709c3
+741.0.0.0.0
+  __TEXT.__text: 0x2b74 sha256:87a1d173031b9a7a67e79107d9ac181db95a65047186bf9ce660750c4f597973
   __TEXT.__auth_stubs: 0x340 sha256:2ed1878a160c10b489413f7b495d0a67d6bb4b0fc3c967726137c80bbaae128d
-  __TEXT.__const: 0x60 sha256:bb212407588c371e7515f66d2a33cfc2e757413a6a779246b01fd231d1ce48ba
+  __TEXT.__const: 0x60 sha256:0c0a809f46aee73480efbdb98310494a5150a5e23ad9ec75258518d6ce6aaeab
   __TEXT.__cstring: 0x11f sha256:d66603d605fa35c5e9700299a5e85a1946b34a716f88929322c5903e8eec9b56
-  __TEXT.__unwind_info: 0xc8 sha256:09a55883fc056d52500728f51b450abde838521742945f9ea2d365801ad0ae3c
-  __DATA_CONST.__cfstring: 0x340 sha256:0eb2d4560c4b74759ca47b850f9ab4ee48e6e1ebef20200bc0e51fd79c048baf
+  __TEXT.__unwind_info: 0xc8 sha256:a31df917195469f304d7f555df136713ff392ee40e1df0aa863f4c6b385792e6
+  __DATA_CONST.__cfstring: 0x340 sha256:4f17463295fab4d49fdb1d3eb17802d5aeea3eda7c2eb8852cfb91a7ecf2b357
   __DATA_CONST.__auth_got: 0x1a0 sha256:44bba2d0723518ffcd909aa02b6166a767ef51cb138f030638409f7e4189807c
   __DATA_CONST.__got: 0x40 sha256:5ab74beef459eadd092e0884c3f6c9efa229f44e01cf1c2122cb77472b450011
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices

   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
-  UUID: 758DFD4E-169B-3BD6-832F-8250AC60B972
+  UUID: 9EEB6C74-B40A-326D-B4CC-989F9663E0A1
   Functions: 36
   Symbols:   83
   CStrings:  53
Functions:
~ _DeviceIDCreateValueList : sha256 4e8502670a5e66acab9fbd81c8c42fde1605a6cc13337003c7c781471a419b7c -> 556a0803443305f6a55143bee74c250f14c24a07a4abfe824019446270042478
~ sub_754 : sha256 2d59b8f3daf313c8de4c3d97e1540b38e9c162a5c788c1bae532ec5c1cbdd759 -> 5ca3259c05271fd60e1308d565385dd57f5bfe33bb3098430da480f68ac5d03b
~ _DeviceIDSupportedValue : sha256 2bc47b79a1d3e712e1e98131be60085a55928489c62f561d1eef7d9d1f7dfd69 -> 81699b1e95526d135022b917903fd0e847c51f3ab15ad791bb343b767e37e07e
~ _DeviceIDSupportedLookup : sha256 6216f9a9d01e73e69760fca2c340930deccb4335627d5b4a523e7cef0ac60568 -> 45e0cbcc575ba7a2600a0802b7667142f88f1cde8600b94c1597af6fd45c2454
~ _USBPrinterClassFactory : sha256 70e5feff477074f83cd8d4376974e4bcc5494802ddbc188906d1b0594f6b8e86 -> b8193047d3e67f4806971c483f09b89671c42e4ac95328b68ed05be48003ff52
~ sub_cfc : sha256 d00d2a2b54a1ab09ba333e4a77313c11642d0b37b87dff83843fa79dacb3878f -> c27a649b22af83aed4edbebef51e65f7233d329c6805cf7502f15b8ac3ae1e99
~ sub_e1c : sha256 458c1310fdb50c1e639686b06a474d99b5923266e395a283af1cec0423e9c8ed -> dc8ed3532416e050346003cf8f33109f7b122134c3255be743c82f3aaf5f3df9
~ sub_e80 : sha256 921d0624ffe71f4f29101ab6a70abe9580d0889d97f5e8e12c84089aaca6a77e -> 2d8120479fc6df673fed193c9ad431924a8710f18c7380223969b2123c163fb5
~ sub_1114 : sha256 4b0ccf83b842a1d934174261b02f5dd341ee7568e55445dd583bcfd02fc2c6da -> e74cbe803f65e4495a9dafcb8fb7dffc9a5ef9d6971efe93373df3b9f14a6830
~ sub_17c0 : sha256 6544e331735f1e0e46f7b542558a25c3593e91b227fef159368c13134af24da6 -> 80d19f5fd65265401c7ede2e83a7ea3a641d55b8e7d448c95a9822d20e89bdb1
~ sub_1a9c : 760 -> 772
~ _UsbSupportedPrinter : sha256 6d5be9ad3172a4344c7a207dd25a91fbf75ca8866816168eb3ae525c9dd967ea -> ad45d3fb94838711bc50cf9882b8163aeaafd5cf1a18e8ff30e1d967d3d4623d
~ _UsbGetPrinterAddress : sha256 2c787c583e3fb8dc276eb3aa3fa52baf5165b2b5c386b57932fef072cac71968 -> 25f21fb37b27ba83996887e251fcaa21135a5fd4c4a656ed1c3fabefa97f0a3e
~ _UsbGetAllPrinters : sha256 53c850bca23d5372e68f1c8f108ba1565b1221ccb93e5148cdefd05142db93c3 -> 8efaf942f4833a6000ae1245c446890bc8ea53fe4d6285119801597dde0e60c7

```
