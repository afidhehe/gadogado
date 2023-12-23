frappe.ui.form.on('JFD QR', {
	ammount: function(frm) {
        // Get the value of the 'ammount' field
        var invoiceAmmount = frm.doc.ammount;
        //var tf1 = invoiceAmmount.toFixed(2);

        // Calculate tax (11% of the invoice amount)
        var taxAmmount = (invoiceAmmount * 11) / 100;
        //var tf2 = taxAmmount.toFixed(2);

        // Set the calculated tax amount in the 'tax' field
        frm.set_value('inv_tax', taxAmmount);
        
        //set the total value
        var totalAmmount = Number(invoiceAmmount) + Number(taxAmmount);
        
        //set the total to total_invoice
        frm.set_value('total', totalAmmount);
        
        //set the Plain text as Requirements
        var sys_id = frm.doc.sys_id;
        var inv = frm.doc.inv;
        var inv_tax_no = frm.doc.inv_tax_no;
        
        // Convert numeric values to 2 decimal places
        invoiceAmmount = parseFloat(invoiceAmmount).toFixed(2);
        taxAmmount = parseFloat(taxAmmount).toFixed(2);
        totalAmmount =parseFloat(totalAmmount).toFixed(2);
        
        
        var concatString = sys_id + '|' + inv + '|' + invoiceAmmount + '|' + totalAmmount + '|' + taxAmmount + '|' + inv_tax_no;
        
        //set the Plain text to QRvalue
        frm.set_value('plain', concatString);
    }
    
})