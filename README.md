# congenial-potato

## Hashtree

![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Hash_Tree.svg/2200px-Hash_Tree.svg.png)

```
Blockheight: 10000
Last Mined: 1525946793.61
Latest Block:
	Root Hash:
		c2263a19bad3a96763bc1a8a2ffe909c9010ba509d0453ea065a22c3d0ea8dad
	Transactions:
		68f6e1698df748604f9479da0a15481ceb5cd5f6575ab240f6138c4db5a9e9cf
		a97e1c9acee6e1e900bde4edb27fb9484fab9fb0da65a1ef15c0fec96d0658f1
		bb22df0bd0cfbeaf6e6b9213a771c5306400554c1e5c9fb335390f16e2c86a11
		0cd5694397f13c51dcb9d6e24aa9639a20a87f3373c058b357adb628bcdbf710
		ef2ddd0e06c8efa3f421486e27289ba1145f42545c319fee866e3f914f69593c
```

add mining

find number where the roothash + some group of characters starts with x zeros where x is difficulty

instead of automatically building blocks, take the last x transactions in while loop while transactions are less then block limit
only accept new block if sha256(roothash + seed) = 000c3daf... where the number of proceeding zeros are equal to difficulty


add real transactions such as sending tokens around
add mining rewards
