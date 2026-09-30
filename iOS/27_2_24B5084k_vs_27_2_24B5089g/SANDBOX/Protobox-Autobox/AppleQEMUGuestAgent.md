## AppleQEMUGuestAgent

> Group: ⬆️ Updated

```diff

 			(literal "/bin/rm")
 			(literal "/usr/bin/pkill")
 		))
+		(require-not (literal "/sbin/reboot"))
 		(require-not (literal "/bin/launchctl"))
 		(require-not (literal "/usr/bin/touch"))
 		(require-not (literal "/usr/bin/plutil"))
```
