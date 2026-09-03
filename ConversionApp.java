import javax.swing.*;
import java.awt.*;
import javax.swing.table.DefaultTableModel;
import javax.swing.event.ChangeListener;
import javax.swing.event.ChangeEvent;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
// most of code such as slider,button,table is from conversion app.
public class ConversionApp {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Conversion App");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800, 600); 
        JPanel panel = new JPanel();
        panel.setLayout(new FlowLayout(FlowLayout.RIGHT));

        JButton button1 = new JButton("Convert");
        button1.setFont(new Font("Times New Roman", Font.BOLD, 25));
        button1.setForeground(Color.WHITE);
        button1.setBackground(new Color(100, 0, 0));
        button1.setPreferredSize(new Dimension(500, 50));

        JSlider slider1 = new JSlider(0, 100, 50); 
        slider1.setPreferredSize(new Dimension(400, 50));
        slider1.setPaintTicks(true);
        slider1.setMinorTickSpacing(10);
        slider1.setPaintTrack(true);
        slider1.setMajorTickSpacing(25);
        slider1.setPaintLabels(true);
        slider1.setFont(new Font("MV Boli", Font.PLAIN, 15));
        slider1.setOrientation(SwingConstants.HORIZONTAL);

        JLabel sliderLabel1 = new JLabel(" = " + slider1.getValue());
        panel.add(sliderLabel1);

        slider1.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                sliderLabel1.setText(" = " + slider1.getValue()); 
            }
        });

        JSlider slider2 = new JSlider(0, 100, 50); 
        slider2.setPreferredSize(new Dimension(400, 50));
        slider2.setPaintTicks(true);
        slider2.setMinorTickSpacing(10);
        slider2.setPaintTrack(true);
        slider2.setMajorTickSpacing(25);
        slider2.setPaintLabels(true);
        slider2.setFont(new Font("MV Boli", Font.PLAIN, 15));
        slider2.setOrientation(SwingConstants.HORIZONTAL);

        JLabel sliderLabel2 = new JLabel(" = " + slider2.getValue());
        panel.add(sliderLabel2);

        slider2.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                sliderLabel2.setText(" = " + slider2.getValue()); 
            }
        });

        JTextField textField = new JTextField();
        textField.setPreferredSize(new Dimension(150, 30));
        panel.add(textField);
        
        String[] columnNames = {"Num 1", "Num 2", "random number", "highest value"};
        DefaultTableModel tableModel = new DefaultTableModel(columnNames, 0);
        JTable table = new JTable(tableModel);
        JScrollPane tableScrollPane = new JScrollPane(table);
        tableScrollPane.setPreferredSize(new Dimension(500, 200));

        panel.add(slider1);
        panel.add(slider2);
        panel.add(button1);
        panel.add(tableScrollPane);

        frame.add(panel);
        frame.setVisible(true);

        button1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int value1 = slider1.getValue();
                int value2 = slider2.getValue();

                int randomNumber = (int) (Math.random() * 100) + 1;// from banking redo

                textField.setText(String.valueOf(randomNumber));

                int highestValue;

                if (value1 >= value2) {
                    if (value1 >= randomNumber) {
                        highestValue = value1;
                    } else {
                        highestValue = randomNumber;
                    }
                } else {
                    if (value2 >= randomNumber) {
                        highestValue = value2;
                    } else {
                        highestValue = randomNumber;
                    }
                }

                Object[] data = {value1, value2, randomNumber, highestValue};
                tableModel.addRow(data);
            }
        });
    }
}
