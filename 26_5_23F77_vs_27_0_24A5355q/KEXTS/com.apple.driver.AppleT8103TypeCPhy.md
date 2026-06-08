## com.apple.driver.AppleT8103TypeCPhy

> `com.apple.driver.AppleT8103TypeCPhy`

```diff

-268.100.17.0.0
+311.0.0.0.0
   __TEXT.__const: 0x1a0
-  __TEXT.__cstring: 0xa577
-  __TEXT.__os_log: 0xe5f4
-  __TEXT_EXEC.__text: 0x43bf0
+  __TEXT.__cstring: 0xaaea
+  __TEXT.__os_log: 0xed5e
+  __TEXT_EXEC.__text: 0x46b90
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8
-  __DATA.__common: 0x38
-  __DATA_CONST.__auth_got: 0xc0
+  __DATA.__data: 0xd8
+  __DATA.__common: 0x60
+  __DATA_CONST.__mod_init_func: 0x10
+  __DATA_CONST.__mod_term_func: 0x10
+  __DATA_CONST.__const: 0x1170
+  __DATA_CONST.__kalloc_type: 0x80
+  __DATA_CONST.__auth_got: 0xd0
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__mod_init_func: 0x8
-  __DATA_CONST.__mod_term_func: 0x8
-  __DATA_CONST.__const: 0x978
-  __DATA_CONST.__kalloc_type: 0x40
-  UUID: 6FC77183-898C-3182-840F-AAD08B7F7FB2
-  Functions: 117
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
