## com.apple.driver.AppleT8103TypeCPhy

> `com.apple.driver.AppleT8103TypeCPhy`

```diff

-268.100.17.0.0
+311.0.0.0.0
   __TEXT.__const: 0x1a0 sha256:f1ae210232cf6960c35e84aaf177973add522bbd0bd4f94ddda7be7fe763414f
-  __TEXT.__cstring: 0xa577 sha256:9754f9aa2fda01232c10aa0758c7c4a72a3af2115467151ccb6ff4a3aa109bca
-  __TEXT.__os_log: 0xe5f4 sha256:e9687887e9773f25eee81e01308da5b4ab066f00c66db66df862c161fa965dc3
-  __TEXT_EXEC.__text: 0x43bf0 sha256:dc0c2d173e7441d2ce37b686aa670fec13860b346c204284fd964c163769728c
+  __TEXT.__cstring: 0xaaea sha256:271009cce6ab50ac857c1228a533bac1364f80624c67d4741f88b9df91aec748
+  __TEXT.__os_log: 0xed5e sha256:47441d8604f73405469bd41a74cf6b459d72d30308d0e4226a38b056e56fe409
+  __TEXT_EXEC.__text: 0x46b90 sha256:9e53a3146f22cde94093498c31ec483bc834750fc6ddbae2cc04eb2bb0285e29
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8 sha256:ba4f736a629bda41f433424f02c64d7bbdec11cd431b1158fcb0e8c4f17c06b3
-  __DATA.__common: 0x38 sha256:d4817aa5497628e7c77e6b606107042bbba3130888c5f47a375e6179be789fbb
-  __DATA_CONST.__auth_got: 0xc0 sha256:5d3ffcbc38d67bdb319a14572f82c6b591cd9bc8022167f900a8297fff1ec274
-  __DATA_CONST.__got: 0x48 sha256:8a0ed41bdf54e237742da241cd909e6cf85e740834c07c4cdc971bb88b82b607
-  __DATA_CONST.__mod_init_func: 0x8 sha256:1193078968a8e41da2543361887dae25afbc1efa06f8845a2c6152a32c729c05
-  __DATA_CONST.__mod_term_func: 0x8 sha256:fc0a177d0477b45ddd5ba65465ffb7cb24a190de90ec6a5c8999ec30bb8dbbaa
-  __DATA_CONST.__const: 0x978 sha256:4bb116cf5be3516922f80d7e0bfa5e9dd1298b73ea07d4cd95bdbc91ca895431
-  __DATA_CONST.__kalloc_type: 0x40 sha256:d87def8611c6896b75f21d0f7518bd0c1698224df40a77ed970b2926e88de9f8
-  UUID: 6FC77183-898C-3182-840F-AAD08B7F7FB2
-  Functions: 117
+  __DATA.__data: 0xd8 sha256:1c5bcbb69173eca6b97afbcc77e1c48a548a4351ec0ceba7c301d5cbc300ba9f
+  __DATA.__common: 0x60 sha256:2ea9ab9198d1638007400cd2c3bef1cc745b864b76011a0e1bc52180ac6452d4
+  __DATA_CONST.__mod_init_func: 0x10 sha256:ac59b3b7b33bfec21b213e31659d20d5c54fc9647e0b85b62425155da0744918
+  __DATA_CONST.__mod_term_func: 0x10 sha256:a5ae3b1e8abbc696f4c017ab2bb4b20e78d86a8732ae9b9a58843070515fad70
+  __DATA_CONST.__const: 0x1170 sha256:a014fdf3272facc94cf3933527d35f7bab7a280aaab3969b66fa77a34d3eb437
+  __DATA_CONST.__kalloc_type: 0x80 sha256:66fee8390aeee57dbaeb9f1ae7c6fc19cd6a7ac5a55aaafab055f891225a0b22
+  __DATA_CONST.__auth_got: 0xd0 sha256:3378891b9525b8fe98afd4f7616c8940568effe93fceb7d3208c0f62e7789b16
+  __DATA_CONST.__got: 0x48 sha256:26c5879f95574cad14d7dffbfa61de42a227eab88c1ea339939040284a1d6be1
+  UUID: 28E8A3B2-AEE8-3B89-80B3-259FBCC7368B
+  Functions: 162
   Symbols:   0
-  CStrings:  1073
+  CStrings:  1115
 
CStrings:
+ "%s@%s: %s::%s: AUSB_CTL_REG_BLK_AUSB_UTMI_MUX_SELECT.EUSB2PHY_SEL = 0x%x\n"
+ "%s@%s: %s::%s: AUSB_CTL_REG_BLK_AUSB_UTMI_MUX_SELECT.UTMI_MUX_SEL = 0x%x\n"
+ "%s@%s: %s::%s: AUSB_CTL_REG_BLK_USB2HOST0_CFG.USB2HOST0_OHCI_PREFETCH_CTRL = 0x%x\n"
+ "%s@%s: %s::%s: AUSB_CTL_REG_BLK_USB2HOST0_CFG.USB2HOST0_OHCI_PREFETCH_EN = 0x%x\n"
+ "%s@%s: %s::%s: AUSB_CTL_REG_BLK_USB2HOST0_CTL.USB2HOST0_HW_CLK_GATE_OFF_EN = 0x%x\n"
+ "%s@%s: %s::%s: AUSB_CTL_REG_BLK_USB2PHY_CTL.USB2PHY_APB_RESET = 0x%x\n"
+ "%s@%s: %s::%s: AUSB_CTL_REG_BLK_USB2PHY_CTL.USB2PHY_RESET = 0x%x\n"
+ "%s@%s: %s::%s: AUSB_CTL_REG_BLK_USB2PHY_CTL.USB2PHY_SIDDQ = 0x%x\n"
+ "%s@%s: %s::%s: AUSB_CTL_REG_BLK_USB2PHY_MISC_TUNE.EUSB2PHY_APBCLK_GATEOFF = 0x%x\n"
+ "%s@%s: %s::%s: AUSB_CTL_REG_BLK_USB2PHY_MISC_TUNE.EUSB2PHY_REFCLK_GATEOFF = 0x%x\n"
+ "%s@%s: %s::%s: AUSB_CTL_REG_BLK_USB2PHY_SIG.VBUS_VALID_EXT_FORCE_EN = 0x%x\n"
+ "%s@%s: %s::%s: AUSB_CTL_REG_BLK_USB2PHY_SIG.VBUS_VALID_EXT_FORCE_VAL = 0x%x\n"
+ "%s@%s: %s::%s: _phySelect: %08x\n"
+ "%s@%s: %s::%s: device memory range 0x%016llx - 0x%016llx\n"
+ "%s@%s: %s::%s: failed to find register range %d\n"
+ "%s@%s: %s::%s: failed to find required register ranges\n"
+ "%s@%s: %s::%s: falling back to compatible register ranges defined by tRegisterSpaces\n"
+ "%s@%s: %s::%s: found register range %d at 0x%016llx (0x%016llx)\n"
+ "12111112122212121111111212121212111211112211222"
+ "AppleT8310TypeCPhy"
+ "eusb2phy_init"
+ "eusb2phy_shutdown"
+ "phy-select"
+ "site.AppleT8310TypeCPhy"

```
