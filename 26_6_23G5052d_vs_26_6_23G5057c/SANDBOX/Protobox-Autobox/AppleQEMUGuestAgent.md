## AppleQEMUGuestAgent

> Group: ⬆️ Updated

```diff

 (deny process-exec*
 	(require-all
 		(require-not (literal "/bin/bash"))
+		(require-not (literal "/bin/ls"))
 		(require-not (literal "/bin/sh"))
 		(require-not (literal "/bin/chmod"))
 		(require-not (literal "/bin/zsh"))
 		(require-not (literal "/usr/bin/killall"))
+		(require-not (literal "/bin/sleep"))
 		(require-any
 			(require-all
 				(require-not (literal "/usr/local/bin/darwinup"))
```
