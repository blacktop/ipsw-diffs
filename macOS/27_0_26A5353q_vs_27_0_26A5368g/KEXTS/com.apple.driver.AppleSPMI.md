## com.apple.driver.AppleSPMI

> `com.apple.driver.AppleSPMI`

```diff

-140.0.0.501.1
+143.0.0.0.0
   __TEXT.__const: 0xf8 sha256:31be7660167365fa7c767612c794ab890bf4b38e017cb4d28cbbcb0543eb3f1a
-  __TEXT.__cstring: 0x1e80 sha256:392b846eb9dac5acf0a66740f9dfaf470857238aabcbcfe327e91b623aab3475
-  __TEXT.__os_log: 0xb71 sha256:cd600d1b1c96d29fd156cff8efba85fc4a8dcbb675970217a5e13a5c100edf7c
-  __TEXT_EXEC.__text: 0xaffc sha256:515d5a81f6fa988ccdcb26227603267ba1ed903499e0725889fc1e8f11d22cac
-  __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc4 sha256:4f035bd57606d41455503f723be857301859a5719d2042d396e97663445c9739
+  __TEXT.__cstring: 0x1efc sha256:68781de995e0d13e4877b3661b0408712a91883cbf198ecba6d60ed282fd4df6
+  __TEXT.__os_log: 0xbc5 sha256:bdc9ed3f588ebb616b284c3e571ae28f9ab2d5ef28a983fdf5b30a2489cbe385
+  __TEXT_EXEC.__text: 0xb148 sha256:b66780b4b0119a2f50e8309b0a1906dd82150336b5f011da21674ae2f56f1d3e
+  __TEXT_EXEC.__auth_stubs: 0x350 sha256:59494487b20035adeb71e5bda118bb5b2574e7d72af36c50daee98c42e91fba5
+  __DATA.__data: 0xc4 sha256:5278238d815303ce99c4de62ee3d91b88e6d558dcb99c892cb1d9786254c52bc
   __DATA.__common: 0x38 sha256:d4817aa5497628e7c77e6b606107042bbba3130888c5f47a375e6179be789fbb
   __DATA.__bss: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
-  __DATA_CONST.__mod_init_func: 0x8 sha256:52d174015ce94db06ea5461b958beb844c7f4d8be4602f0d48620753b8d0f7c7
-  __DATA_CONST.__mod_term_func: 0x8 sha256:2275935c14043a6be6937a533177ab7c1a2284490cc37bb59aa0c1df72d1f5af
-  __DATA_CONST.__const: 0x2210 sha256:b8deed83989de6d310d7bec42759f26645817787b2c7221da76d8d65d8fa68d3
-  __DATA_CONST.__kalloc_type: 0x340 sha256:f28cc3c4176c8b5263efdbf4477a93f14ee93964cae921c8b91f26763a70e0e4
-  __DATA_CONST.__kalloc_var: 0x230 sha256:9e84bf08811c96defe52d11ddef52776e6f7ed9c76c59c34106da03f73dda182
-  __DATA_CONST.__auth_got: 0x1a8 sha256:0cb6f2a67116cb9a43c3ff6655470213dde8afb5a7dc4ae5429d58593e656144
-  __DATA_CONST.__got: 0x40 sha256:3a0b0a80b63b3e17508a8bcccae05452cb8bfa82683239b2e9328eb3da5ae135
-  UUID: 23D548AC-5A35-3852-B802-738EED0DD6B7
-  Functions: 208
-  Symbols:   710
-  CStrings:  332
+  __DATA_CONST.__mod_init_func: 0x8 sha256:6e3dd882b760d49ac4482e402b2360c17500d87ecd72d218bc92a087de0dd5a8
+  __DATA_CONST.__mod_term_func: 0x8 sha256:d4fa978022e339b9f8d611ba0869c0b7b12d14120d2b7087e7b22c4f041a6aa0
+  __DATA_CONST.__const: 0x2210 sha256:65d7e85be271ebfd1145772b7988b4e392c014a23fc1f0f1fbd65d66166c4440
+  __DATA_CONST.__kalloc_type: 0x340 sha256:5c06ff8182b4713c9a96fcbfaf97dba9de79f15df6ba07763954a5a66f73db86
+  __DATA_CONST.__kalloc_var: 0x230 sha256:aaf3de301c049f41c8bcff4f9d520e74c81aae9e0c790fe694afb4ecfb157ef9
+  __DATA_CONST.__auth_got: 0x1a8 sha256:e17ae3672a335119199d8292b3b6639360aec187147d9b0205183f9e55852beb
+  __DATA_CONST.__got: 0x40 sha256:5ca50695b78ed6afc8c57604b22c53b557da2dcf3748fda5ce3dc606121323bc
+  UUID: 8BA78735-8B82-3B50-A8F5-F489F2C5C42E
+  Functions: 211
+  Symbols:   714
+  CStrings:  338
 
Symbols:
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ __ZZN19AppleSPMIController24extendedReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt__18_
+ __ZZN19AppleSPMIController4freeEvE21kalloc_type_view_1542
+ __ZZN19AppleSPMIController4freeEvE21kalloc_type_view_1563
+ __ZZN19AppleSPMIController4freeEvE21kalloc_type_view_1564
+ __ZZN19AppleSPMIController9spmiPanicEPKczE21kalloc_type_view_1619
- __ZZN19AppleSPMIController4freeEvE21kalloc_type_view_1534
- __ZZN19AppleSPMIController4freeEvE21kalloc_type_view_1555
- __ZZN19AppleSPMIController4freeEvE21kalloc_type_view_1556
- __ZZN19AppleSPMIController9spmiPanicEPKczE21kalloc_type_view_1611
CStrings:
+ "BAD"
+ "[%s]:%s:%d:[error]   [%d] = 0x%02X  parity=%s\n"
+ "[%s]:%s:%d:[error] parity error: parity_rcv=0x%04X parity_exp=0x%04X\n"
+ "ok"

```
